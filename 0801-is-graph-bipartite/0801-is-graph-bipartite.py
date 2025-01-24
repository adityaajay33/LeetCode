class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        setA, setB = set(), set()
        seen = set()

        graph_dict = {}
        for i in range(len(graph)):
            graph_dict[i] = graph[i]

        def dfs(n, a):
            seen.add(n)

            for next_node in graph_dict[n]:
                if a and next_node in setA:
                    return False
                if not a and next_node in setB:
                    return False

                if next_node not in seen:
                    if a:
                        setB.add(next_node)
                    else:
                        setA.add(next_node)
                    if not dfs(next_node, not a):
                        return False

            return True

        for key in graph_dict:
            if key not in seen:
                if not dfs(key, True):
                    return False

        return True
