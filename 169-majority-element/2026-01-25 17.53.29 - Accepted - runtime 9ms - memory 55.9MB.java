class Solution {
    public int majorityElement(int[] nums) {
        int count=1;
        int sum=1;
        int ind=nums[0];
        
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                count++;
            }else{
                count=1;
            }
            if(count>sum){
                sum=count;
                ind=nums[i];
            }
            
        }
       
            return ind;
        }
    }