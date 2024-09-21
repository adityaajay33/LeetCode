class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        x, y = heights[1:], heights[:-1]
        diff = [a-b if (a - b) > 0 else 0 for a, b in zip(x, y)]

        count = 0
        heap = []
        for i in diff:
            if i==0:
                count+=1
                continue
            else:
                heapq.heappush(heap, i)
                if len(heap)>ladders:
                    min_diff = heapq.heappop(heap)
                    bricks -= min_diff

                    if bricks <0:
                        return count
                count += 1

                
        return count

        
        