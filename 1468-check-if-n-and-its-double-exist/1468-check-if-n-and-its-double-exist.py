class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        elements = set()

        for item in arr:
            if item*2 in elements or item/2 in elements:
                return True
            else:
                elements.add(item)

        return False
        