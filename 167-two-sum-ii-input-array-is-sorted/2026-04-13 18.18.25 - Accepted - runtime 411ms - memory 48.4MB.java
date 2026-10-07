class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n=numbers.length;
        int k=0;
        int l=0;
      
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(numbers[i]+numbers[j]==target){
                    k=i+1;
                    l=j+1;
                    return new int[] {k,l};
                }
            }
        }
        return new int[]{k,l};
    }
}