class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        if blocks.count('B')==len(blocks):
            return 0

        current_count, max_count, l, r = blocks[:k].count('B'), blocks[:k].count('B'), 0, k-1

        while r<len(blocks)-1:
            
            r+=1
            l+=1 

            if blocks[r]=='B':
                current_count+=1
            if blocks[l-1]=='B':
                current_count -= 1
            
            max_count = max(current_count, max_count)

        return k - max_count

        