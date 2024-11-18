class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        newCode = code[:]

        if k==0:
            newCode = [0 for i in range(len(code))]
        elif k>0:
            for i in range(len(newCode)):
                sumDigit = 0
                for j in range(i+1, i+k+1):
                    sumDigit += code[j%len(code)]
                newCode[i] = sumDigit
        else:
            for i in range(len(newCode)):
                sumDigit = 0
                for j in range(i-1, i+k-1, -1):
                    sumDigit += code[j%len(code)]
                newCode[i] = sumDigit
        
        return newCode

        