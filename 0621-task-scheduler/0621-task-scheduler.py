import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        cooldown = deque()
        time = 0
        
        while max_heap or cooldown:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count < 0:
                    cooldown.append((time + n, count))
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])
        
        return time