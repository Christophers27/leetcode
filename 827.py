from collections import deque


class Solution:
    def largestIsland(self, grid):
        N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            toCheck = deque([(x, y)])

            while toCheck:
                x, y = toCheck.popleft()
                if grid[x][y] == 1:
                    res += 1
                    grid[x][y] = index
                    for xn, yn in move(x, y):
                        if grid[xn][yn] == 1:
                            toCheck.append((xn, yn))

            return res

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res
