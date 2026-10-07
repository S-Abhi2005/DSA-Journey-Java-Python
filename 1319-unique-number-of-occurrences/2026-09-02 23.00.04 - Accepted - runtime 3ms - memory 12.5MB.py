class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        store={}
        for i in arr:
            store[i]=store.get(i,0)+1
        return len(store.values())==len(set(store.values()))
                