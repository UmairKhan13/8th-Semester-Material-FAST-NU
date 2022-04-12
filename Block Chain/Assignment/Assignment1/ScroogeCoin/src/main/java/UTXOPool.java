import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

public class UTXOPool {

    private HashMap<UTXO, Transaction.Output> H;


    public UTXOPool() {
        H = new HashMap<UTXO, Transaction.Output>();
    }

    public void removeUTXO(UTXO utxo) {
        H.remove(utxo);
    }

    public boolean contains(UTXO utxo) {
        return H.containsKey(utxo);
    }

    public Transaction.Output getTxOutput(UTXO ut) {
        return H.get(ut);
    }



    public void addUTXO(UTXO utxo, Transaction.Output txOut) {
        H.put(utxo, txOut);
    }

}
