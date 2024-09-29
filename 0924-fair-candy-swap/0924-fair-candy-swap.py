class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        aliceTotal, bobTotal = 0, 0
        aliceSet, bobSet = set(), set()
        for alice in aliceSizes:
            aliceTotal += alice
            aliceSet.add(alice)
        for bob in bobSizes:
            bobTotal += bob
            bobSet.add(bob)

        desired = (aliceTotal + bobTotal) // 2
        

        #desired -  total = (x - alice)
        res = []
        if aliceTotal==bobTotal:
            return []
        elif aliceTotal>bobTotal:
            for alice in aliceSizes:
                if (desired - aliceTotal + alice) in bobSet:
                    return [alice, desired - aliceTotal + alice]
        else:
            for bob in bobSizes:
                if (desired - bobTotal + bob) in aliceSet:
                    return [desired - bobTotal + bob, bob]

        


        