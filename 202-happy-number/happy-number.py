class Solution:
    def isHappy(self, n: int) -> bool:
        store_value=set()
        while n!=1:
            if n in store_value:
                return False
            store_value.add(n)
            store=0
            while n!=0:

                value=n%10
                store+=value**2
                n=n//10
            n=store
        return True
            
           

        