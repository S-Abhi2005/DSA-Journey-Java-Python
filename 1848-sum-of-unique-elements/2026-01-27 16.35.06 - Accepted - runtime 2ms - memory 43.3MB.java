class Solution {
    public int sumOfUnique(int[] nums) {  
        Map<Integer,Integer>l=new HashMap<>();
        for(int a:nums){
            l.put(a,l.getOrDefault(a,0)+1);
        }  
int sum=0;
        for(Map.Entry<Integer,Integer>e:l.entrySet()){
            if(e.getValue()==1){
                sum+=e.getKey();
            }
        }
        return sum;
    }
}