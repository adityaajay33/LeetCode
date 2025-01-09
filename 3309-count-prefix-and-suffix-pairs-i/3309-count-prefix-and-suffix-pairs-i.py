class Solution:
    def checkPreSuf(self, str1: str, str2: str):
        n1, n2 = len(str1), len(str2)
        if n1>n2:
            return False
        
        return str2[:n1]==str1 and str2[-n1:]==str1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        res = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                res += int(self.checkPreSuf(words[i], words[j]))

        return res