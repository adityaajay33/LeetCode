class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        prefix_sum = 0
        valid = 0

        for i in range(len(nums)-1):
            prefix_sum += nums[i]
            if 2*prefix_sum>=(total_sum):
                valid+=1

        return valid
            