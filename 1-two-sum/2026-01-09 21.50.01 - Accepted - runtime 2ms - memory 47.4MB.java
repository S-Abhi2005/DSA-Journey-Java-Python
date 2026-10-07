class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>m=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int cv=target-nums[i];
            if(m.containsKey(cv)){
                return new int[] {
                    m.get(cv),i};
                   } else{
                        m.put(nums[i],i);
                    }
                   
                
            
        }
         return new int[]{};
        
    }
}