class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        store=[]
        for i in range(n+1):
            count=""
            
            while i>0:
                value=i%2
                count+=str(value)
                i=i//2
            count_value=0
            for j in count:
                if j=='1':
                    count_value+=1
                    
            store.append(count_value)
        return store