# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        diameter = 0
        def dfs(node, depth):
            nonlocal diameter

            if not node.left and not node.right:
                return depth

            left_depth, right_depth = 0, 0

            if node.left:
                left_depth = dfs(node.left, depth+1)
            if node.right:
                right_depth = dfs(node.right, depth+1)
            
            currDiameter = 0
            if left_depth:
                currDiameter+=(left_depth-depth)
            if right_depth:
                currDiameter+=(right_depth-depth)

            diameter = max(diameter, currDiameter)
            return max(left_depth, right_depth)

        dfs(root, 1)
        return diameter


        