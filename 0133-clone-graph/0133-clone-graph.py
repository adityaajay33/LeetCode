"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        cloneHM = {}

        def dfs(node1):
            if node1 in cloneHM:
                return cloneHM[node1]

            copy = Node(node1.val)
            cloneHM[node1] = copy
            
            for neighbor in node1.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None

            
