class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0;
        int sum=0;
        int minl=Integer.MAX_VALUE;//its fix the higher value because if you start value is 0 output will be 0 
        for(int r=0;r<nums.length;r++){
            sum+=nums[r];

            while(sum>=target){
                minl=Math.min(minl,r-l+1);
                sum-=nums[l];
                l++;
            }
        }
        return (minl==Integer.MAX_VALUE?0:minl);
    }
}