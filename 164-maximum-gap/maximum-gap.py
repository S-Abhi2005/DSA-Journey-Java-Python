class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        store=0
        j=0
        num=sorted(nums)
        if len(num)<1:
            return 0
        for i in range(len(num)):
            val=0
            if j!=len(num)-1:
                val=num[j+1]-num[i]
                store=max(val,store)
                j+=1
        return store