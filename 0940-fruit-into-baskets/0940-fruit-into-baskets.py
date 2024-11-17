class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruitSet = {}
        maxFruits, l, r = 0, 0, 0
        while r<len(fruits):
            
            if len(fruitSet)<2:
                fruitSet[fruits[r]] = r
            else:
                if fruits[r] not in fruitSet:
                    rightKey = None
                    for key in fruitSet:
                        if key!=fruits[r-1]:
                            rightKey = key
                    l = fruitSet[rightKey]+1
                    fruitSet[fruits[r]] = r

                    del fruitSet[rightKey]

                else:
                    fruitSet[fruits[r]] = r
                

            r+=1
            maxFruits = max(maxFruits, r-l)

        return maxFruits
            
        