class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(existArr, remArr):

            if not (remArr):
                res.append(existArr)
                return 

            for a in range(len(remArr)):

                dfs(existArr + [remArr[a]], remArr[:a]+remArr[(a+1):])

            return 

        dfs([], nums)

        return res




