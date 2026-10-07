class Solution {
    public int numJewelsInStones(String jewels, String stones) {
     int count=0;
        for(int i=0;i<=jewels.length()-1;i++){
            
            char c=jewels.charAt(i);
            for(int j=0;j<=stones.length()-1;j++){
                char g=stones.charAt(j);
                if(c==g){
                    count++;
                }
            }
        }
        return count;
        
    }
}