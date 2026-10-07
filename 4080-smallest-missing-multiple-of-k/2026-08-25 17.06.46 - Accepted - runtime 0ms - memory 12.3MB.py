class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        value=0
        i=1
        total=True
        while total:
           value=k*i
           i+=1
           if value not in nums:
               break
        return value     
               