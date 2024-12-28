class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(1, n + 1)}
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        res = [0]*n

        for g in range(1, n+1):
            adjacent_colors = set()

            for neighbor in graph[g]:
                if res[neighbor-1]!=0:
                    adjacent_colors.add(res[neighbor-1])

            for color in range(1, 5):
                if color not in adjacent_colors:
                    res[g-1] = color
                    break

        
        return res


        