class Solution:
    def can_make_multiple_palindromes(self, s, lengths):
        freq = Counter(s)
        
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        
        if sum(lengths) > len(s):
            return False
        
        required_odd = sum(length % 2 for length in lengths)
        
        return odd_count <= required_odd

    def canConstruct(self, s: str, k: int) -> bool:

        freq_map = {}
        single_count = 0

        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1

        for freq in freq_map.values():
            if freq % 2 == 1:
                single_count += 1

        return single_count <= k and k <= len(s)


            
            




        



        
        
        