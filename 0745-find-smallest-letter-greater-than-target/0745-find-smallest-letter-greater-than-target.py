import bisect
from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        idx = bisect_right(letters, target)
        return letters[idx] if idx < len(letters) else letters[0]