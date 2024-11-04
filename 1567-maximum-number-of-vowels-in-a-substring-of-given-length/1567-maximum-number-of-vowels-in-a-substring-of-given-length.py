class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        maxVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                maxVowels += 1
        
        vowelCount = maxVowels
        for j in range(k, len(s), 1):
            if s[j] in vowels:
                vowelCount+=1
            if s[j-k] in vowels:
                vowelCount-=1

            maxVowels = max(maxVowels, vowelCount)
        return maxVowels
            