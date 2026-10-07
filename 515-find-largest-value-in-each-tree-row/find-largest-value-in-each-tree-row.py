# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        res=[]
        if root is None:
            return res
        queue=deque([root])
        while queue:
            max_value=float('-inf')
            length=len(queue)
            for _ in range(length):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                max_value=max(max_value,node.val)
            res.append(max_value)
        return res