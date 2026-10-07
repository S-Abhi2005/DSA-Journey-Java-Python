class Solution {
    static HashMap<Character,Integer> sa(String sq){
            HashMap<Character,Integer> s1=new HashMap<>();
            for(int i=0;i<=sq.length()-1;i++){
                Character c=sq.charAt(i);
                s1.put(c,s1.getOrDefault(c,0)+1);
            }
            return s1;
        }
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer> h1=sa(s);
        HashMap<Character,Integer>h2=sa(t);
        return h1.equals(h2);     
    }
}