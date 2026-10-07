class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        j=1
        arr1=[]
        while len(arr1)<k:
            if j not in arr:
                arr1.append(j)
            j=j+1
        return arr1[k-1]