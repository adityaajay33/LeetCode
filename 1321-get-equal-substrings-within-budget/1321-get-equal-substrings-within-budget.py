class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        

        if s==t:
            print(len(s))
            return len(s)

        if not maxCost:
            return 1
        
        
        costArr = collections.deque()

        maxLen = 0
        cost = 0
        r, l = 0, 0

        while r<len(t):
            addCost = abs(ord(s[r])-ord(t[r]))
            print(addCost)
            if addCost>maxCost:
                costArr = collections.deque()
                cost = 0
                l=r+1
                r+=1
                continue
            if addCost+cost>maxCost:
                cumCost = 0
                while (cumCost)<(addCost+cost-maxCost):
                    val = costArr.popleft()
                    cumCost += val
                    cost -= val
                    l+=1
            
            cost += addCost
            costArr.append(addCost)

            r+=1
            maxLen = max(len(costArr), maxLen)

        return maxLen
