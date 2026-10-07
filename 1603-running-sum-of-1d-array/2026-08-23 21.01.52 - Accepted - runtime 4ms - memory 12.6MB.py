class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1=[]
        sum=0
        for i in range(len(nums)):
            
            sum+=nums[i]
            list1.append(sum)

        return list1
            