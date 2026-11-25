class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(math.sqrt(c))
        while i<=j:
            value=i**2 + j**2
            if value==c:
                return True
            elif value<c:
                i+=1
            else:
                j-=1
            
        return False