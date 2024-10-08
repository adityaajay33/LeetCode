class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # If there are no trust relationships and only one person, they are the judge
        if n == 1 and not trust:
            return 1
        
        trust_counts = [0] * (n + 1)
        
        # For each pair, decrement truster and increment trustee
        for truster, trustee in trust:
            trust_counts[truster] -= 1
            trust_counts[trustee] += 1

        # Judge should be trusted by n - 1 people (count = n - 1)
        for person in range(1, n + 1):
            if trust_counts[person] == n - 1:
                return person

        return -1

        