class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        store=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                    store.append(matrix[i][j]) 
        store=sorted(store)
        for i in range(len(store)):
            if i+1==k:
                return store[i]


        
           