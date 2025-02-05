# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        sums = 0
        def binary_search(root):
            nonlocal sums

            if not root:
                return

            if root.val<=low:
                binary_search(root.right)
                if root.val==low:
                    sums+=root.val
            elif root.val>=high:
                binary_search(root.left)
                if root.val==high:
                    sums+=root.val
            else:
                sums+=root.val
                binary_search(root.right)
                binary_search(root.left)

            return sums

        binary_search(root)
        return sums

