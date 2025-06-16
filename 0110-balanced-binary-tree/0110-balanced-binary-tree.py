# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced(root):
            if root is None:
                return True, 0
            left_result, left_depth = is_balanced(root.left)
            right_result, right_depth = is_balanced(root.right)
            result = left_result and right_result and abs(left_depth - right_depth) <= 1
            return result, max(left_depth, right_depth) + 1

        answer, depth = is_balanced(root)
        return answer