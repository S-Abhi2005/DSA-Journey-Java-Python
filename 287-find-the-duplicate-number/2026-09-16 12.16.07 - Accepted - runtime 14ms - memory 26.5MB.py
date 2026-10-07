class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store={}
        for i in nums:
            if i in store:
                return i
            else:
                store[i]=1