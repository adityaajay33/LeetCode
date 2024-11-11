class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def checkPrime(n):
            if n==0 or n==1:
                return False
            for j in range(2, n):
                if n%j==0:
                    return False
            return True

        prime_arr = []
        for i in range(max(nums)):
            if checkPrime(i):
                prime_arr.append(i)

        def findPrime(val):

            nonlocal prime_arr
            ind = bisect.bisect_left(prime_arr, val)

            return prime_arr[ind-1] if (ind-1)>=0 else 0

        
        nums[0] -= findPrime(nums[0])
        for x in range(1, len(nums)):
            val = nums[x] - nums[x-1]
            nums[x] -= findPrime(val)

            if nums[x]<=nums[x-1]:
                print(nums)
                return False

        print(nums)
        return True
            
        