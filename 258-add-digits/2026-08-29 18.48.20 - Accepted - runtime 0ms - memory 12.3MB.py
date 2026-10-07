class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num==0:
            return 0
        
        while num>=10:
            total=0
            while num!=0:
                total+=num%10
                num=num//10
            num=total

        return num