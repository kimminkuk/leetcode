# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([(root)])
        
        while dq:
            node = dq.popleft()
            if node is None:
                continue

            self.arr.append(node)

            temp = node.right 
            temp2 = node.left
            
            node.right = temp2
            node.left = temp
            
            dq.append(node.right)
            dq.append(node.left)
            
        return root