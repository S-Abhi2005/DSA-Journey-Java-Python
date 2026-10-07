class Solution {
    public int[] singleNumber(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<>();
        for(int a:nums){
            h.put(a,h.getOrDefault(a,0)+1);
        }
        int count=0;
         for(int j:h.keySet()){
            if(h.get(j)<=1){
                count++;
            }
         }
         int[] map=new int[count];
         int i=0;
        for(Map.Entry<Integer,Integer> m:h.entrySet()){
                 if(m.getValue()<=1){
                  map[i]=m.getKey();
                  i++;
                 }
        }
        return map;
    }
}