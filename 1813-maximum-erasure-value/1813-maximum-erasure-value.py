class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        '''Find the greatest possible sum of a unique contiguoussubarray
        
        1. if there is a duplicate, it breaks - check for maxValue
            i. move l to the position right after that last seen element
        '''

        l, r = 0, 0
        currSum, maxSum = 0, 0
        seen = set()

        while r<len(nums):
            while nums[r] in seen:
                maxSum = max(currSum, maxSum)
                seen.remove(nums[l])
                currSum -= nums[l]
                l+=1

            seen.add(nums[r])
            currSum += nums[r]

            r+=1

        maxSum = max(currSum, maxSum)
        return maxSum

        