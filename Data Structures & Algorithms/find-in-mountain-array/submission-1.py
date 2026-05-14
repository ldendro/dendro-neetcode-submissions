class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        mountainLen = mountainArr.length()
        l, r = 1, mountainLen - 2
        peak = 0
        while l <= r:
            m = (l + r) // 2
            p = mountainArr.get(m)
            pleft = mountainArr.get(m-1) 
            pright = mountainArr.get(m+1) 
            if pleft < p > pright:
                peak = m
                break
            elif p < pright:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            t = mountainArr.get(m)
            if t == target:
                return m
            elif t < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak + 1, mountainLen - 1
        while l <= r:
            m = (l + r) // 2
            t = mountainArr.get(m)
            if t == target:
                return m
            elif t < target:
                r = m - 1
            else:
                l = m + 1

        return -1

        