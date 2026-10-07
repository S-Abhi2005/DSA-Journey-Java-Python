class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            n=str(nums[i])
            
            if len(n)%2==0:
                count+=1
               
        return count