class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        '''
        you are given an array that looks lik ethis:

        0, 1, 0, 1, 1, 0, 0

        0, 1, 1, 2, 3, 3, 3,

        1, 2, 2, 2, 3
        '''

        num = nums.count(1)

        if num==len(nums):
            return 0

        max_count, current_count, l, r, n = nums[:num].count(1), nums[:num].count(1), 0, num-1, len(nums)
        while r<2*(len(nums)):
            
            l+=1
            r+=1

            if nums[l%n-1]==1:
                current_count -= 1
            if nums[r%n]==1:
                current_count+=1

            max_count = max(current_count, max_count)
    
        return num - max_count