class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int g:nums){
            h.put(g,h.getOrDefault(g,0)+1);
        }
        int j=0;
              for(Map.Entry<Integer,Integer> n:h.entrySet()){
                if(n.getValue()<=1){
                    j=n.getKey();
                }
              }
          
        return j;
    }
}