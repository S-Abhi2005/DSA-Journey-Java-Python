class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        store=[]
        min_total=float('inf')
        for i in range(len(list1)):
            
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    total=i+j
                    if total<min_total:
                        min_total=total
                        store=[list1[i]]
                    elif total==min_total:
                        store.append(list1[i])
                    
        return store
        