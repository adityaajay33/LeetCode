class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def check(x, stores):
            nonlocal quantities 
            num = 0
            for quantity in quantities:
                num += math.ceil(quantity/x)
            return num<=stores

        r = max(quantities)
        l = 1
        while l<r:
            m = (l+r)//2
            if check(m, n):
                r = m
            else:
                l =m+1

        return r