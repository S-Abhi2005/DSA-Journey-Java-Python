class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store={}
        for i in nums:
            if  i in store:
                store[i]+=1
            else:
                store[i]=1
        for key,value in store.items():
            if value==1:
                return key