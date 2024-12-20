class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)

        max_heap = [[-count, char] for char, count in iter(char_count.items())]
        heapq.heapify(max_heap)
        
        print(max_heap)

        res = ""
        while max_heap:
            if len(max_heap)==1 and max_heap[0][0]<-1:
                return ""

            items_del = []
            for i in range(min(2, len(max_heap))):
                max_heap[i][0] += 1
                res += max_heap[i][1]
                if max_heap[i][0] == 0:
                    items_del.append(i)

            for x in range(len(items_del)-1, -1, -1):
                del max_heap[items_del[x]]
            heapq.heapify(max_heap)
        
        return res

        #tuple doesnt allow assignment
        #use del to remove by index
        