class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Binary search to find the right value: O(log(max(n)))

        l, r = 1, max(piles)
        res = r
        while(l<=r):
            m = (l+r)//2
            hours=0
            for pile in piles:
                hours+= math.ceil(pile / m)
            if hours<=h:
                res = min(res, m)
                r = m-1
            else:
                l = m+1
        return res

        #Time complexity: O(log(max(n)) * n)

                    