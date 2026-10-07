import java.math.BigInteger;
class Solution {
    public String multiply(String num1, String num2) {
    //   if (num1.length()>=6||num2.length()>=6){
    
        BigInteger a=new BigInteger(num1);
         BigInteger b=new BigInteger(num2);
       return String.valueOf(a.multiply(b)); 
                 
    
    // }else{
    //    int s=Integer.parseInt(num1);
    //    int r=Integer.parseInt(num2);
    //     int c=r*s;
    //     return String.valueOf(c);
    // }
    }
}