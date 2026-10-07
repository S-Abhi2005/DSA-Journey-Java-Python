class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small=min(nums)
        large=max(nums)
        
        while large!=0:
            rem=small%large
            small=large
            large=rem
        return small