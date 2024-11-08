class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        

        visited = set()
        deadend = set(deadends)
        minPath = 99999999

        if '0000' in deadend:
            return -1

        q = collections.deque()
        q.append(['0000', 0])
        visited.add('0000')

        while q:
            current, steps = q.popleft()
            if current==target:
                return steps
            for i in range(4):
                for move in [-1, 1]:
                    next_digit = (int(current[i]) + move) % 10
                    neighbor = current[:i] + str(next_digit) + current[i+1:]

                    if neighbor not in visited and neighbor not in deadend:
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))
        

        return -1