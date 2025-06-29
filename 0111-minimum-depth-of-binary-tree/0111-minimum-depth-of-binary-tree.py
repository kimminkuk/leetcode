# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        dq = deque([(root, 1)])
        while dq:
            node, level = dq.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                dq.append((node.left, level+1))
            if node.right:
                dq.append((node.right, level+1))
        return

