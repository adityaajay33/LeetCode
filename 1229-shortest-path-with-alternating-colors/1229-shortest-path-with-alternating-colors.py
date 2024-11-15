class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adj = [list() for _ in range(n)]

        for red_edge in redEdges:
            adj[red_edge[0]].append((red_edge[1], 0))

        for blue_edge in blueEdges:
            adj[blue_edge[0]].append((blue_edge[1], 1))

        # Initialization
        ans = [-1] * n
        visited = [[False, False] for _ in range(n)]
        queue = [(0, 0, -1)]
        ans[0] = 0

        # BFS
        while queue:
            node, dist, prev_color = queue.pop(0)

            for neighbor, col in adj[node]:
                if not visited[neighbor][col] and col != prev_color:
                    visited[neighbor][col] = True
                    queue.append((neighbor, dist + 1, col))
                    if ans[neighbor] == -1:
                        ans[neighbor] = dist + 1
        return ans