class Solution {
    public int[] intersection(int[] num1, int[] num2) {
        Set<Integer> st1=new HashSet<>();
        Set<Integer> st2=new HashSet<>();
     for(int num:num1){
        st1.add(num);

     } 
     for(int num:num2){
        if(st1.contains(num)){
            st2.add(num);
        }
     }
     int[] result=new int[st2.size()];
     int i=0;
     for(int num:st2){
        result[i++]=num;

     }
     return result;

    }
}