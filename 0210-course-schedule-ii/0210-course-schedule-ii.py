class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #using topological sort

        adj_list = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1

        queue = collections.deque()
        for key, value in indegree.items():
            if value==0:
                queue.append(key)

        
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for adj_node in adj_list[node]:

                indegree[adj_node]-=1
                if indegree[adj_node]==0:
                    queue.append(adj_node)

        if len(topo_order)==numCourses:
            return topo_order
        else:
            return []


