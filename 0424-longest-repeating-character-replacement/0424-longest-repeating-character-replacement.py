class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = 0
        char_count = defaultdict(int) 
        l = 0  

        for r in range(len(s)):
            char_count[s[r]] += 1

            max_freq = max(char_count.values())
            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len

            

            
        