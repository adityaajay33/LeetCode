class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n==1 and not trust:
            return 1
        elif not trust:
            return -1

        hm = {}

        for truster, trustee in trust:
            trL = hm.get(truster, set())
            trL.add(trustee)
            hm[truster] = trL

        for person in range(1, n+1):
            if person not in hm:
                truth = True
                for pers in range(1, n+1):
                    if (pers!=person and pers not in hm) or (pers!=person and person not in hm[pers]):
                        truth = False
                        break
                if truth:
                    return person

        return -1


        