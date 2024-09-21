class Solution:
    def getLucky(self, s: str, k: int) -> int:

        alphabet_position = {chr(i): i - 96 for i in range(97, 123)}

        sums = ""
        for char in s:
            sums += str(alphabet_position[char])

        final_sum = 0
        for i in range(1, k+1):
            for char in str(sums):
                final_sum += int(char)
            sums = final_sum
            final_sum = 0

        return sums
        