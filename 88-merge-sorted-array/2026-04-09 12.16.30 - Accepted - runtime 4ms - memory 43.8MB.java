class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
    
   int k=0;
    // if(m>n){
        for(int i=0;i<nums1.length;i++){
           if(nums1[i]==0 && k!=nums2.length){
            nums1[i]=nums2[k];
            k++;
           }   
    }
// }else{
//     for(int i=0;i<nums2.length;i++){
//         if(nums2[i]<=0){
//             nums2[i]=nums1[k];
//             k++;
//         }
//     }
// }
Arrays.sort(nums1);
    }
}