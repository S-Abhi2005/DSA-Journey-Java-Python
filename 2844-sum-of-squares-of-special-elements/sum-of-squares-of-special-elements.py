class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        sum_square=0
        for i in range(1,len(nums)+1):
            if n%i==0:
                sum_square+=nums[i-1]*nums[i-1] 
        return sum_square
        