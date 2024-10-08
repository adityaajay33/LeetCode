class Solution:
    def jump(self, nums: List[int]) -> int:
        
        distances = {len(nums)-1: 0}
        prevGoals = set()
        prevGoals.add(len(nums)-1)

        for i in range(len(nums)-2, -1, -1):
            minima=100000
            for j in range(nums[i], 0, -1):
                if (i+j)>=len(nums) or i+j not in prevGoals:
                    continue
                minima = min(1+distances[i+j], minima)
            if minima==100000:
                continue
            prevGoals.add(i)
            distances[i] = minima
                
        return distances[0]

        
