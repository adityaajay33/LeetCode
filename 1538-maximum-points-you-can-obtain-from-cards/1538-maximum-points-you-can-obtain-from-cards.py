class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        start = len(cardPoints)-k 
        initialSum = sum(cardPoints[start:])
        maxSum = initialSum

        sums = initialSum
        for i in range(k):
            sums += (cardPoints[(start+k+i)%len(cardPoints)] - cardPoints[(start+i)%len(cardPoints)])
            maxSum = max(maxSum, sums)

        return maxSum
            




        
        