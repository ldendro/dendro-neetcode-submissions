class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            b = l + (r - l) // 2
            x, y = b // n, b % n 
            if matrix[x][y] < target:
                l = b + 1
            elif matrix[x][y] > target:
                r = b - 1
            else:
                return True

        return False 