class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        max_count = 0
        l, r = 0, 0
        while r < len(s):
          if s[r] not in a:
            a.add(s[r])
            max_count = max(max_count, r-l+1)
            r+=1
          else:
            while s[l]!=s[r]:
              a.remove(s[l])
              l+=1
            l+=1
            r+=1
        return max_count