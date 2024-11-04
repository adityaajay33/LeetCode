class Solution:
    def compressedString(self, word: str) -> str:
        lastChar = ''
        num = 0

        comp = ''

        for char in word:
            if lastChar!='':
                if (char!=lastChar) or (num==9):
                    comp+=str(num)
                    comp+=lastChar

                    num = 1
                    lastChar = char
                else:
                    num+=1
            else:
                lastChar=char
                num=1
        
        comp+=str(num)
        comp+=lastChar

        return comp