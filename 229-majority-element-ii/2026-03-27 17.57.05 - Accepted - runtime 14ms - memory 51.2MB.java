class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> m = new HashMap<>();
        
     
        for (int i : nums) {
            m.put(i, m.getOrDefault(i, 0) + 1);
        }
        
        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        
       
        for (Map.Entry<Integer, Integer> e : m.entrySet()) {
            if (e.getValue() > n / 3) {
                result.add(e.getKey());
            }
        }
        
        return result;
    }
}