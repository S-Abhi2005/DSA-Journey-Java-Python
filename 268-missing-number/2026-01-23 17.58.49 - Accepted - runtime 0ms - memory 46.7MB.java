class Solution {
    public int missingNumber(int[] nums) {
        int v=nums.length;
        int e=v*(v+1)/2;
        int sum=0;
        for(int i=0;i<=nums.length-1;i++){
            sum+=nums[i];
        }

        return e-sum;
        
    }
}