class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])

        min_heap = []

        for i in range(rows):
            for j in range(cols):
                bisect.insort(min_heap, matrix[i][j])
                if len(min_heap)>k:
                    min_heap.pop()

        return min_heap[-1]