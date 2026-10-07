class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        store={}
        for i in arr:
            if i in store:
                store[i]+=1
            else:
                store[i]=1
        maxval=-1
        for key,val in store.items():
            if key==val:
                maxval=max(maxval,key)
        return maxval
                