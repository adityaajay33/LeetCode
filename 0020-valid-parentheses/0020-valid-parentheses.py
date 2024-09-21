class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {
            '{':'}',
            '[':']',
            '(':')'
        }

        st1 = []
        
        for i in s:
          if (i in parDict.keys()):
            st1.append(i)
          elif (i not in parDict.keys()):
            if not st1 or (i!=parDict[st1[-1]]):
              return False
            else:
              

              st1.pop()
        
        if st1==[]:
          return True
        else:
          return False



