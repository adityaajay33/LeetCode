class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        ''' make a hm based on frequency of words. then sort them using a max heap '''

        hm = {}

        for word in words:
            hm[word] = hm.get(word, 0) + 1
        
        heap = []
        for key, value in hm.items():
            heapq.heappush(heap, (-value, key))

        res = []
        for i in range(k):
            val = heapq.heappop(heap)
            res.append(val[1])

        return res