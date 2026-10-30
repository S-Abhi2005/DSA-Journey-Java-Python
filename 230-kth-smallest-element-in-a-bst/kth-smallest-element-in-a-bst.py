# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if root is None:
            return 
        stack=[root]
        store=[]
        while stack:
            top=stack.pop()
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
            store.append(top.val)
        store=sorted(store)
        for i in range(len(store)):
            if i==k-1:
                return store[i]

