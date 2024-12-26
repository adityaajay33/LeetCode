class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        ''' use backtracking here to start from either the positive of the first number and the negative of teh first number. go down the backtracking list of either negative number of the second item or the positive. keep adding until the sum has been reached'''

        res = 0

        @lru_cache(None)
        def backtrack_nums(i, sums):

            if i==len(nums):
                return 1 if sums==target else 0

            add = backtrack_nums(i+1, sums+nums[i])
            subtract = backtrack_nums(i+1, sums-nums[i])
            
            return add+subtract

        return backtrack_nums(0, 0)

            
                