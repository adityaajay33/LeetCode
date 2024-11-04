class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        '''
        maximum speed would be the size of the biggest pile
        minimum speed would be the (sum of all the piles)/hours
        '''

        def checkEat(k):
            hours = 0
            for item in piles:
                hours += math.ceil(item/k)
            return hours<=h

        l, r = max(sum(piles)//h, 1), max(piles)
        while l<r:
            
            m = (l+r)//2

            if checkEat(m):
                r = m
            else:
                l=m+1
        
        return l


        return m
        