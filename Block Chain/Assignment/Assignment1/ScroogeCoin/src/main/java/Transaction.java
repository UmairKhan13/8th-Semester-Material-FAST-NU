import java.security.MessageDigest;
import java.security.PublicKey;
import java.util.Arrays;
import java.util.ArrayList;
import java.security.NoSuchAlgorithmException;
import java.nio.ByteBuffer;

public class Transaction {

    public class Output
    {
        public double value;
        public PublicKey address;


        public Output (double v, PublicKey addressGiven)
        {
            value = (double)v;
            address = addressGiven;
        }
    }


    public class Input{
        public byte[] previousTransactionHash;
        public int outIndexPosition;
        public byte[] signature;


        public void addSignature(byte [] sig)
        {
            if(sig == null)
            {
                signature = null;
            }
            else
            {
                signature = Arrays.copyOf(sig, sig.length);
            }
        }

        public Input(byte[] previousHash, int position)
        {
            if(previousHash == null)
            {
                previousTransactionHash = null;
            }
            else
            {
                previousTransactionHash = Arrays.copyOf(previousHash, previousHash.length);
            }

            outIndexPosition = position;
        }
    }


    public byte[] hash;
    public ArrayList<Input> inputArrayList;
    public ArrayList<Output> outputArrayList;

    public Transaction(Transaction transaction1)
    {
        hash = transaction1.hash.clone();
        inputArrayList = new ArrayList<Input>(transaction1.inputArrayList);
        outputArrayList = new ArrayList<Output>(transaction1.outputArrayList);
    }

    public Transaction()
    {
        inputArrayList = new ArrayList<Input>();
        outputArrayList = new ArrayList<Output>();
    }


    public byte[] getHash() {
        return hash;
    }

    public ArrayList<Input> getInputArrayList() {
        return inputArrayList;
    }

    public ArrayList<Output> getOutputArrayList() {
        return outputArrayList;
    }

    public Input getInput(int index) {
        if (index < inputArrayList.size()) {
            return inputArrayList.get(index);
        }
        return null;
    }

    public Output getOutput(int index) {
        if (index < outputArrayList.size()) {
            return outputArrayList.get(index);
        }
        return null;
    }

    public int numInputs() {
        return inputArrayList.size();
    }

    public int numOutputs() {
        return outputArrayList.size();
    }

    public void addInput(byte [] previousTransactionHash, int outputIndex)
    {
        Input in = new Input(previousTransactionHash, outputIndex);
        inputArrayList.add(in);
    }

    public void addOutput(double value, PublicKey address)
    {
        Output op = new Output((double)value, address);
        outputArrayList.add(op);
    }

    public void removeInput(int position)
    {
        inputArrayList.remove(position);
    }

    public void removeInput(UTXO utxoRemoveInput)
    {
        for (int index = 0; index< inputArrayList.size(); index++)
        {
            Input in = inputArrayList.get(index);
            UTXO u = new UTXO(in.previousTransactionHash, in.outIndexPosition);
            if(u.equals(utxoRemoveInput))
            {
                inputArrayList.remove(index);
                return;
            }
        }
    }


    public void addSignature(byte[] signature, int index) {
        inputArrayList.get(index).addSignature(signature);
    }

    public byte[] getRawDataToSign(int position)
    {
        ByteBuffer b = ByteBuffer.allocate(Integer.SIZE / 8);

        ArrayList<Byte> signedBytes = new ArrayList<Byte>();
        if(position > inputArrayList.size())
        {
            return null;
        }

        Input inputValue = inputArrayList.get(position);
        b.putInt(inputValue.outIndexPosition);


        byte[]  previousTransactionHash = inputValue.previousTransactionHash;
        byte[] outputIndex = b.array();

        if (previousTransactionHash != null)
            for (int index = 0; index < previousTransactionHash.length; index++)
                signedBytes.add(previousTransactionHash[index]);
        for (int index = 0; index < outputIndex.length; index++)
            signedBytes.add(outputIndex[index]);

        for (Output operation : outputArrayList) {
            
            ByteBuffer byteBuffer = ByteBuffer.allocate(Double.SIZE / 8);
            byteBuffer.putDouble(operation.value);
            
            
            byte[] value = byteBuffer.array();
            byte[] addressBytes = operation.address.getEncoded();
            
            for (int index = 0; index < value.length; index++)
                signedBytes.add(value[index]);

            for (int i = 0; i < addressBytes.length; i++)
                signedBytes.add(addressBytes[i]);
        }
        byte[] signatureData = new byte[signedBytes.size()];
        int i = 0;
        for (Byte sb : signedBytes)
            signatureData[i++] = sb;
        return signatureData;
    }

    public byte[] getRawTx() {
        ArrayList<Byte> notCommittedTransaction = new ArrayList<Byte>();

        for (Output operation : outputArrayList) {
            ByteBuffer b = ByteBuffer.allocate(Double.SIZE / 8);
            b.putDouble(operation.value);
            byte[] value = b.array();
            byte[] addressBytesReceiver = operation.address.getEncoded();
            for (int i = 0; i < value.length; i++) {
                notCommittedTransaction.add(value[i]);
            }
            for (int i = 0; i < addressBytesReceiver.length; i++) {
                notCommittedTransaction.add(addressBytesReceiver[i]);
            }

        }

        for (Input in : inputArrayList) {
            byte[] prevTxHash = in.previousTransactionHash;
            ByteBuffer b = ByteBuffer.allocate(Integer.SIZE / 8);
            b.putInt(in.outIndexPosition);
            byte[] outputIndex = b.array();
            byte[] signature = in.signature;
            if (prevTxHash != null)
                for (int i = 0; i < prevTxHash.length; i++)
                    notCommittedTransaction.add(prevTxHash[i]);
            for (int i = 0; i < outputIndex.length; i++)
                notCommittedTransaction.add(outputIndex[i]);
            if (signature != null)
                for (int i = 0; i < signature.length; i++)
                    notCommittedTransaction.add(signature[i]);
        }

        byte[] transaction = new byte[notCommittedTransaction.size()];
        int i = 0;
        for (Byte b : notCommittedTransaction)
            transaction[i++] = b;
        return transaction;
    }

    public void finalize() {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(getRawTx());
            hash = md.digest();
        } catch (NoSuchAlgorithmException x) {
            x.printStackTrace(System.err);
        }
    }
}