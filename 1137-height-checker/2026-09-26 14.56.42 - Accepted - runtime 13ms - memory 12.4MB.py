class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        store=list(heights)
        for i in range(len(heights)-1):
            for j in range(len(heights)-1-i):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1], heights[j]
        count=0
        j=0
        for i in range(len(heights)):
            if store[j]!=heights[i]:
                count+=1
            j+=1
        return count 