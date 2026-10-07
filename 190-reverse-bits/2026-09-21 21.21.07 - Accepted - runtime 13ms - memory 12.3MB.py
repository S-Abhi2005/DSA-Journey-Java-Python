class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        value=""
        while n>0 or len(value)<32:
            total=n%2
            value+=str(total)
            n=n//2
        value=value[::-1]
        value2=value
        final_value=0
        power=0
        for j in range(len(value)):
            if value[j]=='1':
                final_value+=2**power    
            power+=1
        return final_value
            
        