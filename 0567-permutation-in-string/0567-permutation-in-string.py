class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        # Frequency counters for s1 and the initial window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])

        # Sliding window over s2
        for i in range(len_s1, len_s2):
            if s1_count == window_count:
                return True

            # Add the next character to the window
            window_count[s2[i]] += 1

            # Remove the character that's no longer in the window
            window_count[s2[i - len_s1]] -= 1

            # If the count goes to zero, remove it from the window_count
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]

        # Final check for the last window
        return s1_count == window_count