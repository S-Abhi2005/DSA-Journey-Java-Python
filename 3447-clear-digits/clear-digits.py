class Solution:
    def clearDigits(self, s: str) -> str:
        store=[]
        for i in s:
            if i.isdigit():
                store.pop()
            else:
                store.append(i)
        final_string=''.join(store)
        return final_string