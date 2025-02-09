class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        '''
        Count the number of bad pairs

        n = length of nums

        Bad pairs = total number of pairs - total number of good pairs
        total number of pairs = sum of all values from 1 to (n-1)
        '''
        '''
        #Brute force

        bad = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[j]-nums[i])!=(j-i):
                    bad+=1

        return bad
        '''


        #Mathematical approach
        n = len(nums)
        res = [0]*n
        total_pairs = ((n*(n+1))/2)-(n)

        for i in range(n):
            res[i] = nums[i]-i

        hm = {}
        for ind, val in enumerate(res):
            hm[val] = hm.get(val, 0) + 1
        
        good_pairs = 0
        for key, val in hm.items():
            good_pairs += (((val*(val+1))/2)-(val))

        return int(total_pairs-good_pairs)