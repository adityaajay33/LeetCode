class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        k = n-k

        def quickSelect(l, r):

            pivotIndex = random.randint(l, r)
            nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]

            pivot = nums[r]
            p = l
            lessEnd = -1

            for i in range(l, r):
                num = nums[i]
                if num < pivot:
                    lessEnd = p
                if num<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1

            nums[p], nums[r] = nums[r], nums[p]

            if k>p:
                return quickSelect(p+1, r)
            elif k>lessEnd:
                return nums[p]
            else:
                return quickSelect(l, lessEnd)
        return quickSelect(0, n-1)