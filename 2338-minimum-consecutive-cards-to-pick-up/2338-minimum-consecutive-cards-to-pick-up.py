class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        hm = {}
        minCards = -1

        for i in range(len(cards)):
            if cards[i] in hm:
                if minCards==-1:
                    minCards = i-hm[cards[i]]+1
                else:
                    minCards = min(i-hm[cards[i]]+1, minCards) 

            hm[cards[i]] = i

        return minCards

        