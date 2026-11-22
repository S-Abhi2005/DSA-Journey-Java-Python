class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_Average=float('-inf')

        sum_val=sum(nums[:k])
        max_Average=sum_val

        for j in range(k,len(nums)):
            sum_val=sum_val-nums[j-k]+nums[j]
            max_Average=max(max_Average,sum_val)

        return max_Average/k

      
