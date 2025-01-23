class Solution:
    def countServers(self, grid):
        R, C = len(grid), len(grid[0])
        rowCount, colCount = [0] * R, [0] * C
        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    rowCount[r] += 1
                    colCount[c] += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (rowCount[r] > 1 or colCount[c] > 1):
                    res += 1

        return res
