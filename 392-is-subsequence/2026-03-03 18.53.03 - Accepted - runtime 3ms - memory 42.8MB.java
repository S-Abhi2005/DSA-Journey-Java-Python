class Solution {

    public boolean isSubsequence(String s, String t) {
         String g="";
         int j=0;
       for(int i=0;i<=s.length()-1;i++){
            char c=s.charAt(i);
            while(j<=t.length()-1){
                char k=t.charAt(j);
                j++;
                if(c==k){
                    g+=k;
                    break;
                }
            }
          
        }
       return s.equals(g);
    }
    
    
}