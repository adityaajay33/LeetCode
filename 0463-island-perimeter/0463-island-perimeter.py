class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])


        def bfs(r, c):
            nonlocal perimeter
            perimeter = 0
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = q.popleft()
                local_perimeter = 4
                for dr, dc in directions:
                    new_r, new_c = row+dr, col+dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c]==1:
                        local_perimeter-=1
                        if (new_r, new_c) not in visited:
                            q.append((new_r, new_c))
                            visited.add((new_r, new_c))
                perimeter+=local_perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r, c) not in visited:
                    bfs(r, c)
        
        return perimeter


        