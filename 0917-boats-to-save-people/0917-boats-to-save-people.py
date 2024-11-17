class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            # If the lightest and heaviest person can share a boat
            if people[l] + people[r] <= limit:
                l += 1
            # The heaviest person always gets on a boat
            r -= 1
            boats += 1
