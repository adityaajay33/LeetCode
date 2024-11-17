class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        res = []
        def backtrack(s, arr):
            if not s:
                res.append(arr[:])
                return
            for i in range(len(s)):
                if isPalindrome(s[:i+1]):
                    arr.append(s[:i+1])
                    backtrack(s[i+1:], arr)
                    arr.pop()

        backtrack(s, [])
        return res


        
        