class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        '''probably will need a max heap and have to traverse by bfs'''

        
        freq = {}
        visited = set()

        def bfs():
            neighbors = friends[id]
            visited.add(id)
            for i in neighbors:
                visited.add(i)

            q = collections.deque()
            q += neighbors

            for i in range(level):
                nextQ = collections.deque()
                for neighbor in q:
                    for nextNeighbor in friends[neighbor]:
                        if nextNeighbor not in visited:
                            nextQ.append(nextNeighbor)
                            visited.add(nextNeighbor)
                    if i<level-1:
                        continue
                    for item in watchedVideos[neighbor]:
                        freq[item] = freq.get(item, 0) +  1
                q = nextQ

        bfs()
        
        result = sorted(freq.keys(), key=lambda x: (freq[x], x))
        return result
        



        