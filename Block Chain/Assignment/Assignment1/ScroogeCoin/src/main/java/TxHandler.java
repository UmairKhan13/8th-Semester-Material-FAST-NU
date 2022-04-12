import java.security.*;
import java.util.*;

public class TxHandler {

    private UTXOPool utxoPool;

    public TxHandler(UTXOPool utxoPool1)
    {
        utxoPool = utxoPool1;
    }

    public boolean isValidTx(Transaction transaction)
    {
        float inSum = 0;
        float outSum =0;
        Set<UTXO> claimedUTXO = new HashSet<UTXO>();

        List<Transaction.Input> inputs = transaction.getInputArrayList();
        for(int i=0; i<inputs.size(); i++)
        {
            boolean check = false;
            Transaction.Input input = inputs.get(i);
            try{
                check = verifySignatureOfConsumeCoin(transaction, i, input);

            }
            catch (Exception exception)
            {
                System.out.println(exception.toString());
            }
            /*
               catch(InvalidKeyException exception)
               {
                    System.out.println(exception.toString());
               }

             */



            if(!isConsumedCoinAvailable(input))
            {
                return false;
            }

            if(!check)
            {
                return false;
            }
            if(isCoinConsumedMultipleTimes(claimedUTXO, input))
            {
                return false;
            }

            UTXO utxo = new UTXO(input.previousTransactionHash, input.outIndexPosition);
            Transaction.Output corresponingOutput = utxoPool.getTxOutput(utxo);
            inSum += corresponingOutput.value;

        }

        List<Transaction.Output> outputs = transaction.getOutputArrayList();
        for (int i = 0; i < outputs.size(); i++) {
            Transaction.Output output = outputs.get(i);
            if (output.value <= 0) {
                return false;
            }

            outSum += output.value;
        }

        // Should the input value and output value be equal? Otherwise the ledger will
        // become unbalanced.
        // The difference between inputSum and outputSum is the transaction fee
        if (outSum > inSum) {
            return false;
        }

        return true;
    }

    private boolean isCoinConsumedMultipleTimes(Set<UTXO> claimedUTXO, Transaction.Input input) {
        UTXO utxo = new UTXO(input.previousTransactionHash, input.outIndexPosition);
        return !claimedUTXO.add(utxo);
    }

    private boolean verifySignatureOfConsumeCoin(Transaction tx, int index, Transaction.Input input) {
        UTXO utxo = new UTXO(input.previousTransactionHash, input.outIndexPosition);
        Transaction.Output correspondingOutput = utxoPool.getTxOutput(utxo);
        PublicKey pk = correspondingOutput.address;
        return Crypto.verifySignature(pk, tx.getRawDataToSign(index), input.signature);
    }

    private boolean isConsumedCoinAvailable(Transaction.Input input) {
        UTXO utxo = new UTXO(input.previousTransactionHash, input.outIndexPosition);
        return utxoPool.contains(utxo);
    }

    public Transaction[] handleTxs(Transaction[] possibleTxs) {
        List<Transaction> acceptedTx = new ArrayList<Transaction>();
        for (int i = 0; i < possibleTxs.length; i++) {
            Transaction tx = possibleTxs[i];
            if (isValidTx(tx)) {
                acceptedTx.add(tx);

                removeConsumedCoinsFromPool(tx);
                addCreatedCoinsToPool(tx);
            }
        }

        Transaction[] result = new Transaction[acceptedTx.size()];
        acceptedTx.toArray(result);
        return result;
    }

    private void addCreatedCoinsToPool(Transaction tx) {
        List<Transaction.Output> outputs = tx.getOutputArrayList();
        for (int j = 0; j < outputs.size(); j++) {
            Transaction.Output output = outputs.get(j);
            UTXO utxo = new UTXO(tx.getHash(), j);
            utxoPool.addUTXO(utxo, output);
        }
    }

    private void removeConsumedCoinsFromPool(Transaction tx) {
        List<Transaction.Input> inputs = tx.getInputArrayList();
        for (int j = 0; j < inputs.size(); j++) {
            Transaction.Input input = inputs.get(j);
            UTXO utxo = new UTXO(input.previousTransactionHash, input.outIndexPosition);
            utxoPool.removeUTXO(utxo);
        }
    }

}