class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        currSum = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            currSum += gas[i]-cost[i]

            if currSum<0:
                start=i+1
                currSum=0

        return start





            
        