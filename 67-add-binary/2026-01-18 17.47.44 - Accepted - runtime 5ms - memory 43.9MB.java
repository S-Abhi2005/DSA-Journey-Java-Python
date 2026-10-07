import java.math.BigInteger;
class Solution {
    public String addBinary(String a, String b) {
         BigInteger r=new BigInteger(a,2);
         BigInteger s=new BigInteger(b,2);
         BigInteger sum=r.add(s);
         return sum.toString(2);
    }
}