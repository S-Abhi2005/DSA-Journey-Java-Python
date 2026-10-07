class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for(int i=0;i<nums.length;i++){
            int id=Math.abs(nums[i])-1;
            if(nums[id]>0){
                nums[id]=-nums[id];
            }
        }
         List<Integer>l1=new ArrayList<>();
         for(int i=0;i<nums.length;i++){
            if(nums[i]>0){
                l1.add(i+1);
            }
         }

        return l1;
    }
}