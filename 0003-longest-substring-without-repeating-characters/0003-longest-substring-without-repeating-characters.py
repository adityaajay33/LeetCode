class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        l, r = 0, 1
        seen = set()
        maxLen = 1

        seen.add(s[l])

        while r<len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            maxLen = max(r-l+1, maxLen)

            r+=1

        return maxLen
        