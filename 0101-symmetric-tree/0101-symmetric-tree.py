# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # mirror 는 left와 right가 일치하는건가??
        # child의 left, right가 서로 일치 해야합니다.
        # 처음에는 그냥 나누고???
        # 함수를 두개로 나눌까?
        # 
        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        return is_mirror(root.left, root.right)