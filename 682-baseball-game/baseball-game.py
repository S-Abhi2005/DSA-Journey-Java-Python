class Solution:
    def calPoints(self, operations: list[str]) -> int:
        store=[]
        for i in operations:
            if i=='C':
                val=store.pop()
            elif i=='D':
                store.append(2 * store[-1])
            elif i=='+':
                store.append(store[-2]+store[-1])
            elif i=='-':
                store.append(store[-2]-store[-1])
            elif i=='*':
                store.append(store[-2]*store[-1])
            elif i=='/':
                store.append(store[-2]/store[-1])
            else:
                store.append(int(i))
        return sum(store)