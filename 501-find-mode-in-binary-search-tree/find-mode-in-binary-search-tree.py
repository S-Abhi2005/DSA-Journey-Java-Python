# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return 0
        Mode_values={}
        final_values=[]
        store=[root]
        max_value=0
        while store:
            top=store.pop()
            if top.val not in Mode_values:
                Mode_values[top.val]=1
            else:
                Mode_values[top.val]+=1
            if top.right:
                store.append(top.right)
            if top.left:
                store.append(top.left)
        max_value=max(Mode_values.values())
       
        for key,val in Mode_values.items():
            
            if val==max_value:
                final_values.append(key)
        return final_values


        