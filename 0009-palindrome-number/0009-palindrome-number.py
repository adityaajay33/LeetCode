#print(f{a}, file=sys.stderr, flush=True)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        l, r = 0, len(str(x))-1
        num = str(x)
        while l<=r:
            if num[l]!=num[r]:
                return False
            l+=1
            r-=1
                
        return True