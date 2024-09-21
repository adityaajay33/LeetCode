
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=1
        if root==None:
            return 0
        list_nodes = [root]
        while(len(list_nodes)!=0):
            current = list_nodes.pop(0)
            if(current.left!=None):
                list_nodes.append(current.left)
                count+=1
            if(current.right!=None):
                list_nodes.append(current.right)
                count+=1
            
        return count
