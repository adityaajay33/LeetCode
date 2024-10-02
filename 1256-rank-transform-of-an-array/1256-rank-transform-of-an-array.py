class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        res = [0 for j in arr]

        hm = {}
        for i in range(len(arr)):
            result = hm.get(arr[i], [])
            result.append(i)
            hm[arr[i]] = result

        sorted_dict = {key: hm[key] for key in sorted(hm.keys())}

        count = 1
        for key, val in sorted_dict.items():
            for i in val:
                res[i] = count
            count+=1

        return res
