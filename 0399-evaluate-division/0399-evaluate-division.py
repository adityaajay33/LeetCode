class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        calc = {}

        for ind, tup in enumerate(equations):
            a, b = tup[0], tup[1]

            if a not in calc:
                calc[a] = {}
            if b not in calc:
                calc[b] = {}
            calc[a][b] = values[ind]
            calc[b][a] = 1/values[ind]

        def dfs(c_in, d_out, prod, visited):
            if c_in not in calc:
                return -1.0
            if d_out in calc[c_in]:
                return prod*(calc[c_in][d_out])

            visited.add(c_in)

            for key, val in calc[c_in].items():
                if key not in visited and key in calc:
                    out = dfs(key, d_out, prod*calc[c_in][key], visited)

                    if out!=-1:
                        return out


            return -1.0



        
        res = []
        for c, d in queries:
            out = dfs(c, d, 1, set())
            res.append(out)

        return res
        