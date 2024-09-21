class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        us = [[j, i] for i, j in enumerate(score)]
        us.sort(key=lambda x:x[0], reverse=True)

        answer = [0]*n
        for i in range(len(us)):
            if i==0:
                answer[us[i][1]]= "Gold Medal" 
            elif i==1:
                answer[us[i][1]]= "Silver Medal" 
            elif i==2:
                answer[us[i][1]]= "Bronze Medal" 
            else:
                answer[us[i][1]]= f"{i+1}" 
        
        return answer