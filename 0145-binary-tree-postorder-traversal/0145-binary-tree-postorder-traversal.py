# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            traversal(root.right)
            arr.append(root.val)
        traversal(root)
        return arr