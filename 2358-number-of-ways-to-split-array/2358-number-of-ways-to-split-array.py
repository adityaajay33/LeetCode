class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_phase, right_phase, sums = [0]*n, [0]*n, 0
        for i in range(n):
            sums += nums[i]
            left_phase[i] = sums

        sums = 0
        for i in range(n-1, -1, -1):
            sums+=nums[i]
            right_phase[i] = sums

        valid = 0
        for i in range(1, n):
            valid += 1 if left_phase[i-1] >= right_phase[i] else 0

        return valid


        