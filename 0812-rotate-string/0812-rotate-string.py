class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        char = goal[0]
        ind = collections.deque()

        for c in range(len(s)):
            if s[c]==char:
                ind.append(c)

        if not ind:
            return False

        while ind:
            item = ind[0]
            for a in range(len(s)):
                if s[(ind[0]+a)%len(s)]!=goal[a]:
                    ind.popleft()
                    break
            if (a==len(s)-1) and s[(item+a)%len(s)]==goal[a]:
                return True

        return False