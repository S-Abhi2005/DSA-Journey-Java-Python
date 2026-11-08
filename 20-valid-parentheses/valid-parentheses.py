class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)<=1:
            return False
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif len(stack)>=1:
                if (stack[-1]=='(' and i==')' )or (stack[-1]=='[' and i==']' ) or (stack[-1]=='{' and i=='}' ):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if len(stack)!=0:
            return False
        return True