class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        matchsticks.sort(reverse=True)
        
        total_matchsticks = sum(matchsticks)
        side_length = total_matchsticks//4

        def dfs(n, sides, index):

            if index==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]==side_length

            for i in range(4):
                if sides[i] + matchsticks[index] > side_length:
                    continue
                sides[i] += matchsticks[index]
                if dfs(n+1, sides, index+1):
                    return True
                sides[i] -= matchsticks[index]

                if sides[i]==0:
                    break
            return False

        return dfs(0, [0, 0, 0, 0], 0)