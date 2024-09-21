class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        listStr = []
        for n in nums:
            listStr.append(str(n))

        def compare(x, y):
            if x+y>y+x:
                return -1
            else:
                return 1

        largestNum = ''.join(sorted(listStr, key = cmp_to_key(compare)))

        if largestNum[0]=='0':
            return '0'
        return largestNum
        