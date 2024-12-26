class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = {}
        dp = {}
        res = [i for i in range(len(quiet))]

        for x, y in richer:
            interim = graph.get(y, [])
            graph[y] = interim + [x]

        print(graph)

        def track_quietest(x):
            if x in dp:
                return dp[x]

            if x not in graph or not graph[x]:
                dp[x] = x
                return x
            
            for item in graph[x]:
                smallest = track_quietest(item)

                if quiet[smallest]<quiet[res[x]]:
                    res[x] = smallest
                
            dp[x] = res[x]
            return dp[x]

        for j in range(len(quiet)):
            res[j] = track_quietest(j)

        return res

