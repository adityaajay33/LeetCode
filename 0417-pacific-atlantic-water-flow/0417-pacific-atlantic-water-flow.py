class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                row, col = dr+ r, dc + c
                if (row in range(rows) and col in range(cols) and heights[row][col]>=heights[r][c] and (row, col) not in visited):
                    dfs(row, col, visited)

        
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1, c, atl)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols-1, atl)

        return list(pac & atl)