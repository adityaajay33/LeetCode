class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, val in enumerate(nums):
            if target - val in hm:
                return [i, hm[target-val]]
            hm[val] = i
            