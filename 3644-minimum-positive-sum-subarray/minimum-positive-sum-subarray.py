class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_subarray=float('inf')
        store=[]
        for i in range(len(nums)):
            store=[]
            for j in range(i,len(nums)):
                store.append(nums[j])
                if l<= len(store)<=r:
                    if sum(store)>0:
                            min_subarray=min(min_subarray,sum(store))
        if min_subarray==float('inf'):
            return -1
        
        return min_subarray
