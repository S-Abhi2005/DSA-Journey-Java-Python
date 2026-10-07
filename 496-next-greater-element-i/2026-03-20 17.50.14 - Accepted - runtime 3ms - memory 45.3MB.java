class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] num3=new int[nums1.length];
            HashMap<Integer,Integer> m=new HashMap<>();
            for(int i=0;i<nums2.length;i++){
                m.put(nums2[i],i);
            }
        for(int i=0;i<=nums1.length-1;i++){
          
           for(int j=m.get(nums1[i])+1;j<nums2.length;j++){
            if(nums2[j]>nums1[i]){
                num3[i]=nums2[j];
                break;
            }
           }
        }
        for(int i=0;i<num3.length;i++){
            if(num3[i]==0){
                num3[i]=-1;
            }
        }
        return num3;
        
    }
}