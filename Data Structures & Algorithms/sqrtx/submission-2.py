class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x // 2
        if x == 0 or x == 1:
            return x
        while True:
            m = l + (r - l) // 2
            ans = x // m 
            if x >= (ans * ans) and x < ((ans+1)*(ans+1)):
                return ans
            elif ans > m:
                l = m + 1
            else:
                r = m - 1