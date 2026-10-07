class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        total=""
        while num!=0:
            value=num%2
            if value==0:
                total+=str(1)
            else:
                total+=str(0)
            num=num//2
        j=0
        store=0
        for i in total:
            store+=int(i)*2**j
            j=j+1
        return store
            
        