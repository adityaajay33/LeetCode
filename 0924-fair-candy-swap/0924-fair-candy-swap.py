class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        # Calculate delta
        delta = (sumB - sumA) // 2
        
        # Create a set of Bob's candy sizes for quick lookup
        bobSet = set(bobSizes)
        
        # Find a valid pair (x, y) such that x + delta = y
        for x in aliceSizes:
            if x + delta in bobSet:
                return [x, x + delta]

            


        