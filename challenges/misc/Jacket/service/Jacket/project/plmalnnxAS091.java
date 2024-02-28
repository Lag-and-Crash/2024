import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.util.Base64;

class plmalnnxAS091 {

    public String lsadmlasjijd(String s1, SecretKey s3, IvParameterSpec s2) {
        try {
            Cipher lcnalisd = Cipher.getInstance("AES/CBC/PKCS5PADDING");
            lcnalisd.init(Cipher.ENCRYPT_MODE, s3, s2);
            byte[] ncaluisd = lcnalisd.doFinal(s1.getBytes());
            return Base64.getEncoder().encodeToString(ncaluisd);
        } catch (Exception e) {
            System.out.println(e);
            return "FAILURE";
        }
        
    }
}