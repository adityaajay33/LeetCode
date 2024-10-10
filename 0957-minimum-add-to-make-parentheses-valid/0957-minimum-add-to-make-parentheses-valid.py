class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        openCount = 0
        closeCount = 0

        for char in s:
            if char=="(":
                openCount+=1
            else:
                if openCount>0:
                    openCount-=1
                else:
                    closeCount+=1

        return openCount + closeCount
