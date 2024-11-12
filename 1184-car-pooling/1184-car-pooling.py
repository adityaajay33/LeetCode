class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x:x[1])
        location = []

        current_cap = 0

        for x, y, z in trips:
            while location and y>=location[0][0]:
                passengers = heapq.heappop(location)
                current_cap -= passengers[1]

            heapq.heappush(location, (z, x))
            current_cap += x

            if current_cap>capacity:
                return False

        return True
            


            
        