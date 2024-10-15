# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(value, node, listAnc):
            if not node:
                return None

            listAnc.append(node)
            if node==value:
                return listAnc

            x = dfs(value, node.left, listAnc)
            if x:
                return x
            
            y = dfs(value, node.right, listAnc)
            if y:
                return y
            
            listAnc.pop()
            return None

        a = dfs(p, root, [])
        b = dfs(q, root, [])

        if not a or not b:
            return None

        rangeL = min(len(a), len(b))
        LCA = root
        for i in range(rangeL):
            if a[i]==b[i]:
                LCA = a[i]
        
        return LCA

        