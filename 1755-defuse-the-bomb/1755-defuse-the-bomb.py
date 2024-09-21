class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0 for a in code]
        elif k>0:
            sum = 0
            for i in range(1, k+1):
                sum+=code[i]
            list_vals = []
            list_vals.append(sum)
            for j in range(1, len(code)):
                sum+= (code[(j+k)%len(code)] - code[j])
                list_vals.append(sum)
            return list_vals
        else:
            sum = 0
            for i in range(abs(k), 0, -1):
                sum+=code[-i]
            list_vals = []
            list_vals.append(sum)
            for j in range(1, len(code)):
                sum+= (code[(j-1)] - code[j+k-1])
                list_vals.append(sum)
            return list_vals
