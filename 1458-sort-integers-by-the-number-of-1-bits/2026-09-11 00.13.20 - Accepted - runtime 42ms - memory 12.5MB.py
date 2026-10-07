class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        store=[]
        for i in range(len(arr)):
            res=""
        
            n=arr[i]
            while n>0:
                rem=n%2
                res+=str(rem)
                n=n//2
            count=0
            for j in range(len(res)):
                if res[j]=='1':
                    count+=1
            
            store.append([arr[i],count])
                
        store.sort(key=lambda x: (x[1],x[0]))
        ans=[]
        for k in store:
            ans.append(k[0])
        return ans