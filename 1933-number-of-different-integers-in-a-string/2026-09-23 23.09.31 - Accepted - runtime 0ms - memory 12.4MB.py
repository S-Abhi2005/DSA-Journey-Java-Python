class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        store=set()
        count=0
        value=""
        for i in range(len(word)):
            
            if word[i].isdigit():
                value+=word[i]
            else:
                if value!="":
                    val=int(value)
                    val=str(val)
                    if val not in store:
                        store.add(val)
                        count+=1
                    value=""
                        
        if value!="":
            val=int(value)
            val=str(val)
            if val not in store:
                store.add(val)
                count+=1
        return count   