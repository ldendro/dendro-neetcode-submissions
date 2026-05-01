class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def iterate(m):
            kcount = k
            ksum = 0
            for num in nums:
                if (ksum + num) > m:
                    kcount -= 1
                    ksum = num
                    if kcount == 0:
                        return False
                else:
                    ksum += num
            return True
                    
        l, r = max(nums), sum(nums)
        ans = r
        while l <= r:
            m = l + (r - l) // 2
            if iterate(m):
                r = m - 1
                ans = m 
            else:
                l = m + 1

        return ans
