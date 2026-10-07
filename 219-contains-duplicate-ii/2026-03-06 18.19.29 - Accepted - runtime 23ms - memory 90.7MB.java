import java.util.HashMap;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        
        HashMap<Integer, Integer> m = new HashMap<>();
        
        for(int i=0;i<nums.length;i++){
            if(m.containsKey(nums[i])){
                int prv=m.get(nums[i]);
                if(i-prv<=k){
                    return true;
                }
            }
            m.put(nums[i],i);
        }
        return false;
    }
}