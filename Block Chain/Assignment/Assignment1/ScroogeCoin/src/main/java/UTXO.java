import java.util.Arrays;

public class UTXO implements Comparable<UTXO> {


    private byte[] transactionHash;


    private int position;

    public UTXO(byte[] transactionHash, int position) {
        this.transactionHash = Arrays.copyOf(transactionHash, transactionHash.length);
        this.position = position;
    }


    public byte[] getTransactionHash() {
        return transactionHash;
    }


    public int getPosition() {
        return position;
    }


    public int compareTo(UTXO utxo) {
        int in = utxo.position;
        byte[] hash = utxo.transactionHash;
        if (in > position)
            return -1;
        else if (in < position)
            return 1;
        else {
            int length2 = hash.length;
            int length1 = transactionHash.length;


            if (length2 > length1)
                return -1;
            else if (length2 < length1)
                return 1;
            else {
                for (int index = 0; index < length1; index++) {
                    if (hash[index] > transactionHash[index])
                        return -1;
                    else if (hash[index] < transactionHash[index])
                        return 1;
                }
                return 0;
            }
        }
    }

    public int hashCode() {
        int hash = 1;
        hash = hash * 17 + position;
        hash = hash * 31 + Arrays.hashCode(transactionHash);
        return hash;
    }


    public boolean equals(Object objOther) {
        if (objOther == null) {
            return false;
        }
        if (getClass() != objOther.getClass()) {
            return false;
        }

        UTXO utxoOther = (UTXO) objOther;
        byte[] hash = utxoOther.transactionHash;
        int in = utxoOther.position;
        if (hash.length != transactionHash.length || position != in)
            return false;
        for (int index = 0; index < hash.length; index++) {
            if (hash[index] != transactionHash[index])
                return false;
        }
        return true;
    }


}
