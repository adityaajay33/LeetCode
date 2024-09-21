class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Total number of rolls
        total_rolls = len(rolls) + n
        
        # The total sum of all n + m rolls should be mean * total_rolls
        total_sum = mean * total_rolls
        
        # The sum of known rolls
        known_sum = sum(rolls)
        
        # The sum of missing rolls
        missing_sum = total_sum - known_sum
        
        # The sum of missing rolls should be between n * 1 and n * 6
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Result array for missing rolls
        result = [missing_sum // n] * n
        
        # Distribute the remainder to make sure the sum is exactly missing_sum
        remainder = missing_sum % n
        
        # Increment the first 'remainder' elements by 1 to account for the leftover sum
        for i in range(remainder):
            result[i] += 1
        
        return result