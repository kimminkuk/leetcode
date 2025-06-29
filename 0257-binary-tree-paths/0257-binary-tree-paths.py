# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        dq = deque([(root, "")])
        while dq:
            node, direct = dq.popleft()
            if node is None:
                ans.append(direct)
                continue
            if node.left is None and node.right is None:
                ans.append(direct + str(node.val))
            else:
                if node.left:
                    dq.append((node.left, direct + str(node.val) + "->"))
                if node.right:
                    dq.append((node.right, direct + str(node.val) + "->"))
        return ans