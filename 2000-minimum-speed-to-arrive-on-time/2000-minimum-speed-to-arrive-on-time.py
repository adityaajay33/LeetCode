class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        if len(dist)>math.ceil(hour):
            return -1


        def check_arrival(speed):

            nonlocal dist, hour

            hours = 0
            for i in range(len(dist)-1):
                hours+= math.ceil(dist[i]/speed)
            hours+=dist[-1]/speed

            return hours <= hour

        l, r = 1, 10000000
        while l<r:

            m=(l+r)//2
            arr = check_arrival(m)
            if arr:
                r = m
            else:
                l = m+1
        return l


        