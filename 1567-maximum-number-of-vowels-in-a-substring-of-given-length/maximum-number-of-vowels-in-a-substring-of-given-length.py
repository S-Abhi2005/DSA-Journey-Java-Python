class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        count=0
        max_val=0
        for i in range(k):
            if s[i] in v:
                count+=1
        max_val=count
        for i in range(k,len(s)):
            if s[i-k] in v:
                count-=1
            if s[i] in v:
                count+=1
            max_val=max(max_val,count)
        return max_val