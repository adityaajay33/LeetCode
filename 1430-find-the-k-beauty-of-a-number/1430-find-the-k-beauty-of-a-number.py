class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kb = 0
        number = str(num)
        for i in range(len(number) - k + 1):
            div = int(number[i:i+k])
            if div!=0 and (num%div==0):
                kb+=1
        return kb
        