import bisect
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:


        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        res = []

        queue = []
        currTime = 0
        i = 0

        while i<len(tasks) or queue:
            while i<len(tasks) and tasks[i][0]<=currTime:
                heapq.heappush(queue, (tasks[i][1], tasks[i][2]))
                i+=1

            if queue:
                processingOut, indexOut = heapq.heappop(queue)
                currTime+=processingOut
                res.append(indexOut)
            else:
                currTime = tasks[i][0]

        return res
        