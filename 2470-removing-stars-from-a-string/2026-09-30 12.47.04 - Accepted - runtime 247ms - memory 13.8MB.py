class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        store=[]
        for i in s:
            if i!='*':
                store.append(i)
            else:
                store.pop()
        result=''.join(store)
        return result