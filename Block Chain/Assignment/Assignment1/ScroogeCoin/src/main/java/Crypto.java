import java.security.PublicKey;
import java.security.SignatureException;
import java.security.NoSuchProviderException;
import java.security.Signature;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;

public class Crypto {

    public static boolean verifySignature(PublicKey pubKey, byte[] message, byte[] signature) {

        Signature signature1 = null;


        try {
            signature1 = Signature.getInstance("SHA1withDSA", "SUN");
        }catch (NoSuchProviderException exception) {
            exception.printStackTrace();
        }
        catch (NoSuchAlgorithmException exception) {
            exception.printStackTrace();
        }

        try {
            signature1.initVerify(pubKey);
        } catch (InvalidKeyException exception) {
            exception.printStackTrace();
        }
        try {
            signature1.update(message);
            return signature1.verify(signature);
        } catch (SignatureException exception) {
            exception.printStackTrace();
        }
        return false;

    }
}

