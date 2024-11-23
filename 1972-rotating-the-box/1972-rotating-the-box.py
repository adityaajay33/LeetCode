class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        modified = []

        for row in box:
            modRow = []
            rocks, spaces, obstacles = 0, 0, 0
            for cell in row:
                if cell=='.':
                    spaces+=1
                elif cell=='#':
                    rocks+=1
                else:
                    obstacles+=1
                    modRow += (['.' for _ in range(spaces)] + ['#' for _ in range(rocks)])
                    modRow += ['*']
                    spaces, rocks = 0, 0

            modRow += (['.' for _ in range(spaces)] + ['#' for _ in range(rocks)])
            modified.append(modRow)

        print(modified)


        res = []
        for y in range(len(modified[0])):
            a = []
            for x in range(len(modified)-1, -1, -1):
                a.append(modified[x][y])
            res.append(a)
        
        return res
        