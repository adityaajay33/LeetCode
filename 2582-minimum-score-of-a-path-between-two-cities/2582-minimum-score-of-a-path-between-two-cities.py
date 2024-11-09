class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        neighbors = {}

        for x, y, z in roads:
            val = neighbors.get(x, {})
            val[y] = z
            neighbors[x] = val

            val = neighbors.get(y, {})
            val[x] = z
            neighbors[y] = val

        visited = set()
        minPath = 100000
        print(neighbors)

        def dfs(node):
            nonlocal minPath
            visited.add(node)

            for key in neighbors[node]:
                minPath = min(minPath, neighbors[node][key])
                if key not in visited:
                    dfs(key)

        dfs(1)

        return minPath

        