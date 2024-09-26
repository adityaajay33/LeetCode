class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        dnaSet = set()
        l, r = 0, 10
        res = set()

        while r<=len(s):
            if s[l:r] in dnaSet and s[l:r] not in res:
                res.add(s[l:r])

            dnaSet.add(s[l:r])
            l+=1
            r+=1


        res = list(res)
        return res
        