class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        openBrackets, closeBrackets = collections.deque(), collections.deque()

        for i in range(len(s)):
            if s[i]=='(':
                openBrackets.append(i)
            elif s[i]==')':
                if openBrackets:
                    openBrackets.pop()
                else:
                    closeBrackets.append(i)

        newString = ""
        for j in range(len(s)):
            if openBrackets and j==openBrackets[0]:
                openBrackets.popleft()
                continue
            if closeBrackets and j==closeBrackets[0]:
                closeBrackets.popleft()
                continue
            
            newString+=s[j]

        return newString

        
        


        