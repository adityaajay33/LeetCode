class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        totals = [gas[x]-cost[x] for x in range(n)]
        
        l, r = 0, 0
            
        #find the large continguous subarray of sum greater than 0

        currSum = 0
        while r<(2*len(gas)):
            if (r-l)==n:
                return l

            currSum += totals[r%n]
            r+=1

            if currSum<0:
                while l<r:
                    currSum -= totals[l%n]
                    l+=1

        return -1





            
        