# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_depth = float('inf')
        self.cur_depth = 1
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth_with_level(root, level):
            if root:
                if not root.left and not root.right:
                    self.min_depth = min(self.min_depth, level)                    
                    #print(f"min_depth:{self.min_depth}")
                min_depth_with_level(root.left, level+1)
                min_depth_with_level(root.right, level+1)
        min_depth_with_level(root, 1)
        #print(f"[2] min_depth:{self.min_depth}")
        if self.min_depth == float('inf'):
            return 0
        else:
            return self.min_depth