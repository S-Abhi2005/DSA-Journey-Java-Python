class Solution:
    def removeDuplicates(self, s: str) -> str:
        store=[]
        for i in range(len(s)):
            if len(store)==0:
                store.append(s[i])
            elif s[i]==store[-1]:
                store.pop()
            else:
                store.append(s[i])
        return ''.join(store)

