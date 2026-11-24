class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        sum_val=sum(arr[:k])
        j=sum_val//k
        count=0
        for i in range(k,len(arr)):
            if j>=threshold:
                count+=1
            sum_val=sum_val-arr[i-k]+arr[i]
            j=sum_val//k
        if j>=threshold:
            count+=1
        return count
            
        