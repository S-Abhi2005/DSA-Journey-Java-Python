class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        store=[]
        for i in nums:
            store.append(i**2)
        store.sort()
        return store