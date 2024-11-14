class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0

        prevCount = 0
        currentCount = 0

        for row in bank:
            currentCount = row.count('1')
            
            beams += (currentCount * prevCount)
            prevCount = currentCount if currentCount else prevCount
            currentCount = 0


        return beams
