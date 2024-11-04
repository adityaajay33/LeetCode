class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        if len(s)>12:
            return res 

        def backtrack(ip, dots, original):
            if dots == 0:  # No more dots to place
                if ip and (ip == '0' or (ip[0] != '0' and int(ip) < 256)):
                    res.append(original + ip)
                return

            for char in range(1, min(4, len(ip) + 1)):
                seg = ip[:char]
                # Check if segment is valid
                if seg == '0' or (seg[0] != '0' and int(seg) < 256):
                    backtrack(ip[char:], dots - 1, original + seg + ".")

        backtrack(s, 3, "")
        return res

