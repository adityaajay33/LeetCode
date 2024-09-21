class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        t = timestamp
        res=""
        if key in self.timemap:
            timelist = self.timemap[key]

            l, r = 0, len(timelist)-1
            while (l<=r):
                m = (l+r)//2

                if timelist[m][1]<=timestamp:
                    res= timelist[m][0]
                    l=m+1
                elif timelist[m][1]>timestamp:
                    r=m-1
            return res
        else:
            return ""
            