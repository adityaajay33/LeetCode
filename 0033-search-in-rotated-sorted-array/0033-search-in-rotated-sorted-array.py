class Solution:
    def binary_search(self, nums, l, r, target):

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m

            if nums[l] <= nums[m]:  
                if nums[l] <= target < nums[m]:
                    return self.binary_search(nums, l, m-1, target)
                else:  
                    l = m + 1
            else: 
                if nums[m] < target <= nums[r]:  
                    return self.binary_search(nums, m+1, r, target)
                else: 
                    r = m - 1


        return -1