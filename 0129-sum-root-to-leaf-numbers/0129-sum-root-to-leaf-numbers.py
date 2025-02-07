# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        arr = []

        def dfs(node, curr):
            nonlocal arr

            if not node.left and not node.right:
                arr.append(int(curr+str(node.val)))
                return 
            if node.left:
                dfs(node.left, curr+str(node.val))
            if node.right:
                dfs(node.right, curr+str(node.val))

        dfs(root, "")
        return sum(arr) 