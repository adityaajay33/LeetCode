class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = set()
        seen = set()

        graph_dict = {}
        for i in range(len(graph)):
            graph_dict[i] = graph[i]

        
        def dfs(n):
            if graph_dict[n]==[]:
                safe.add(n)
                return True

            safeBool = None
            for next_node in graph_dict[n]:
                print(f"main: {n} and secondary: {next_node}")
                if next_node not in seen:
                    seen.add(next_node)
                    if not dfs(next_node):
                        return False
                elif next_node not in safe:
                    return False

            safe.add(n)
            return True


        for i in range(len(graph)):
            if i in seen:
                continue
            dfs(i)

        safe = list(safe)
        safe.sort()
        return list(safe)