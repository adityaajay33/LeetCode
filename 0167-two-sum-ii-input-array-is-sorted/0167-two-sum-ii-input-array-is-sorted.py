class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hm:
                return [hm[target - numbers[i]]+1, i+1]
            else:
                hm[numbers[i]] = i
            