class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        Total_Sum=0
        for i in nums:
            store=[]
            j=1
            while j*j<=i:
                if i%j==0:
                    store.append(j)
                    if j!=i//j:
                        store.append(i//j)
                j+=1
            if len(store)==4:
                Total_Sum+=sum(store)
        return Total_Sum


                
        