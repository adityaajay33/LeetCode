class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0

        prevCount = 0
        currentCount = 0

        for row in bank:
            for device in row:
                if int(device):
                    currentCount += 1
            beams += (currentCount * prevCount)
            prevCount = currentCount if currentCount else prevCount
            currentCount = 0


        return beams
