class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        store=[]
        value=0
        for i in s:
            if i=='(':
                if value>0:
                     store.append(i)
                value+=1
            else:
                value-=1
                if value>0:
                    store.append(i)

            
        return ''.join(store)
        