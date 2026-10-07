class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n<0 or n==0:
            return False
        i=1
        while 4**i<=n:
            if 4**i==n:
                return True
            i=i+1
        return False
                
        