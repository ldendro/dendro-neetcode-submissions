class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        self.freshBananas = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([i,j])
                    seen.add((i,j))
                if grid[i][j] == 1:
                    self.freshBananas += 1

        if self.freshBananas == 0:
            return 0

        def addRotten(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] == 0:
                return False

            seen.add((r,c))
            q.append([r,c])
            self.freshBananas -= 1

            return True

        res = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addRotten(r-1, c)
                addRotten(r+1, c)
                addRotten(r, c-1)
                addRotten(r, c+1)
            res += 1
            if self.freshBananas == 0:
                return res

        return -1