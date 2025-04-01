# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search(root):
            if root:
                if root.left:
                    search(root.left)
                print('root',root)
                self.arr.append(root.val)     
                if root.right:
                    search(root.right)
                #self.arr.append(root)
        search(root)
        return self.arr


        