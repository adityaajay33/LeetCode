class Solution:
    def findLHS(self, nums: List[int]) -> int:
        elements = {}
        common_value = 0
        for i in nums:
            elements[i] = elements.get(i, 0) + 1
            
        for j in elements:
            if j+1 in elements:
                common_value = max([common_value, elements[j]+elements[j+1]])
        return common_value
            