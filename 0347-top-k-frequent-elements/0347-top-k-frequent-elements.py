import bisect
class Solution:
    def topKFrequent(self, nums, k):
        hm = {}
        l = []
        m = []
        for a in nums:
            hm[a] = hm.get(a, 0) + 1
        for key in hm:
            ind = bisect.bisect_left(m, hm[key])
            l.insert(ind, key)
            m.insert(ind, hm[key])
            if len(l) > k:
              l.pop(0)
              m.pop(0)
        return l