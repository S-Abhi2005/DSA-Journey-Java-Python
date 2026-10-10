# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        queue=deque([root])
        value_root=root.val
        sum_leaf=0
        while queue:
            length=len(queue)
            for i in range(length):
                value=0
                node=queue.popleft()
                if node.left:
                    if node.left.left is None and node.left.right is None:
                        sum_leaf+=node.left.val
                    else:
                        queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
        return sum_leaf
                
        
        