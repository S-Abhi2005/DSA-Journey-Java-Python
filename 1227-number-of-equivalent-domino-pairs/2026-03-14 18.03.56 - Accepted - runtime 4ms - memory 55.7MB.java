class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
       
       int[] s=new int[100];
       int rs=0;
       int b=0,c=0;
        for(int[] a:dominoes){
            b=Math.min(a[0],a[1]);
            c=Math.max(a[0],a[1]);

            int k=b*10+c;
            rs+=s[k];
            s[k]++;
        }
        return rs;
          }
}