class Solution {
    public int reverse(int x) {
      int a=0;
      while(x!=0){
        int sum=x%10;
        x/=10;
        if(a>Integer.MAX_VALUE/10 ||a<Integer.MIN_VALUE/10){
            return 0;
        }
        a=a*10+sum;
      }
    return a;
        
    }
}