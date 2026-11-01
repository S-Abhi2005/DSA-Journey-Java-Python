# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        queue=deque([root])
        store=[]
        while queue:
            size = len(queue)
            total = 0

            for i in range(size):
                top = queue.popleft()
                total += top.val

                if top.left:
                    queue.append(top.left)

                if top.right:
                    queue.append(top.right)

            store.append(total / size)

        return store