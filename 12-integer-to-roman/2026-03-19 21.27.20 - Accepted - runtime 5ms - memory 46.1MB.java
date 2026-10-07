class Solution {
    public String intToRoman(int num) {
        int[] val={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] sy={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        String sum="";
        for(int i=0;i<val.length;i++){
            while(num>=val[i]){
                sum+=sy[i];
                num-=val[i];
            }
        }
          return sum;
        
    }
}