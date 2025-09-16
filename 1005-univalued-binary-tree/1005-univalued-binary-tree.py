# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def judgeParentChildNode(self, root, pre_val):
        if not root:
            return True
        if root.val != pre_val:
            return False
        return self.judgeParentChildNode(root.left, root.val) and self.judgeParentChildNode(root.right, root.val)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.judgeParentChildNode(root, root.val)

        