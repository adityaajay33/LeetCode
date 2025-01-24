# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Build the graph
        graph_dict = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph_dict[node.val].append(parent.val)
                graph_dict[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: Perform BFS to find nodes at distance k
        visited = set()
        queue = [(target.val, 0)]  # Use a list as a queue (node value, current distance)
        visited.add(target.val)

        result = []

        while queue:
            # Simulate deque's popleft using list slicing
            node, dist = queue[0]
            queue = queue[1:]  # Remove the first element

            if dist == k:
                result.append(node)

            if dist < k:
                for neighbor in graph_dict[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result