class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        arr = []
        l = len(original)/n
        for i in range(int(l)):
            arr.append(original[(i*n):(i+1)*n])

        return arr
        