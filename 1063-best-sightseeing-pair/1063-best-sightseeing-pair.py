class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        j_vals = [y-x for x, y in enumerate(values)]

        #print(values)
        #print(j_vals)

        max_val = j_vals[-1]
        max_total = 0

        for i in range(len(values)-2, -1, -1):
            max_val = max(j_vals[i+1], max_val)
            max_total = max(values[i]+i+max_val, max_total)

            #print(max_total)

        return max_total

        