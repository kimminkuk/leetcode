# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
    def binary_arr_sum(self, binary_arr):
        res = 0
        for i in range(len(binary_arr)):
            res += binary_arr[-1-i] << i
        self.answer += res

    def depth_leaf(self, root, arr):
        if root:
            arr.append(root.val)
            if not root.left and not root.right:
                self.binary_arr_sum(arr)    
            else:
                self.depth_leaf(root.left, arr)
                self.depth_leaf(root.right, arr)
            arr.pop()
            
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depth_leaf(root, [])
        return self.answer