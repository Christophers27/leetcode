from collections import deque


class Solution:
    def findMaxFish(self, grid):
        res = 0
        R, C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    count = 0
                    frontier = deque([(r, c)])

                    while frontier:
                        x, y = frontier.popleft()
                        if grid[x][y] > 0:
                            count += grid[x][y]
                            grid[x][y] = 0

                            if x > 0 and grid[x - 1][y] > 0:
                                frontier.append((x - 1, y))
                            if x + 1 < R and grid[x + 1][y] > 0:
                                frontier.append((x + 1, y))
                            if y > 0 and grid[x][y - 1] > 0:
                                frontier.append((x, y - 1))
                            if y + 1 < C and grid[x][y + 1] > 0:
                                frontier.append((x, y + 1))

                    res = max(res, count)

        return res
