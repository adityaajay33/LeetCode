class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if not nums or not p:
            return 0

        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i=0
            while i<len(nums)-1:
                if nums[i+1]-nums[i]<=max_diff:
                    i+=2
                    count+=1
                else:
                    i+=1
            return count>=p


        l, r = 0, nums[-1] - nums[0]
        while l<r:
            m=(l+r)//2
            x = can_form_pairs(m)
            if x:
                r = m
            else:
                l=m+1
        
        return l

        
