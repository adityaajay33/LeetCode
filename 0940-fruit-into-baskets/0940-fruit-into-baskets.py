class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitSet = {}
        l, maxFruits = 0, 0

        for r in range(len(fruits)):
            # Add current fruit to the basket
            fruitSet[fruits[r]] = fruitSet.get(fruits[r], 0) + 1

            # If there are more than 2 types of fruits, shrink the window
            while len(fruitSet) > 2:
                fruitSet[fruits[l]] -= 1
                if fruitSet[fruits[l]] == 0:
                    del fruitSet[fruits[l]]
                l += 1

            # Update the maximum fruits collected
            maxFruits = max(maxFruits, r - l + 1)

        return maxFruits