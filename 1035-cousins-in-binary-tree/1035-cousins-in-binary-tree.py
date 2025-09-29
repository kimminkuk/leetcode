# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x_parent=0
        self.y_parent=0
        self.x_depth=0
        self.y_depth=0
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def find_cousin(node, parent, depth):
            if node:
                if node.val == x:
                    self.x_parent = parent
                    self.x_depth = depth
                elif node.val == y:
                    self.y_parent = parent
                    self.y_depth = depth
                find_cousin(node.left, node, depth+1)
                find_cousin(node.right, node, depth+1)
        
        find_cousin(root, None, 0)
        # print(f"self.x_parent:{self.x_parent} y_parent:{self.y_parent}")
        # print(f"self.x_depth:{self.x_depth} y_depth:{self.y_depth}")
        if self.x_parent != self.y_parent and self.x_depth == self.y_depth:
            return True
        else:
            return False
        

        