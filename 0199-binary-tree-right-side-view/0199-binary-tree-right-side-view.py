# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        def bfs(node):
            nonlocal res
            q = collections.deque()
            
            q.append(node)
            res.append(q[-1].val)

            while q:
                for _ in range(len(q)):
                    curr = q.popleft()

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                
                if q:
                    res.append(q[-1].val)
                

        bfs(root)
        return res
            

        
