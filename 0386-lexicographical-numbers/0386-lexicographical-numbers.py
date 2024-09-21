class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        res = []

        def dfs(num):
        
            if num>n:
                return 
            
            res.append(num)

            for j in range(10):
                if int(str(num)+str(j))>n:
                    break
                dfs(int(str(num)+str(j)))

        for i in range(1, 10):
            dfs(i)

        return res
        




        