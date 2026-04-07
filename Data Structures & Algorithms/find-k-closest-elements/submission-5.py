class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1
        # 1 1 1 10 10 10
        for i in range(k, len(arr)):
            if abs(arr[i] - x) < abs(arr[r] - x) or abs(arr[i] - x) < abs(arr[l] - x) or arr[i] == arr[i-1]:
                l += 1
                r += 1
            else:
                return arr[l:r+1]

        return arr[l:r+1]