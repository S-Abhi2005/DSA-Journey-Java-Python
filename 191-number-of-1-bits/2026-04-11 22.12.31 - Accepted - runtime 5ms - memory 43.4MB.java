class Solution {
    public int hammingWeight(int n) {
        String Bits="";
        if(n==0){
            return 0;
        }
        
        while(n>0){
        int rem=n%2;
        Bits+=rem;
        n/=2;
        }
        int count=0;
        for(int i=0;i<Bits.length();i++){
            char c=Bits.charAt(i);
            if(c=='1'){
                count++;
            }
        }
       return count; 
    }
}