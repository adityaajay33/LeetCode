class Solution:
   def removeOccurrences(self, s: str, part: str) -> str:

        while 1:
                if part in s:
                    s=s.replace(part, "", 1)
                else:
                    break
            return s