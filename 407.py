import heapq


class Solution:
    def trapRainWater(self, grid):
        R, C = len(grid), len(grid[0])

        if R < 3 or C < 3:
            return 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        boundary = []

        for r in range(R):
            heapq.heappush(boundary, (grid[r][0], r, 0))
            heapq.heappush(boundary, (grid[r][C - 1], r, C - 1))
            grid[r][0] = grid[r][C - 1] = -1

        for c in range(1, C - 1):
            heapq.heappush(boundary, (grid[0][c], 0, c))
            heapq.heappush(boundary, (grid[R - 1][c], R - 1, c))
            grid[0][c] = grid[R - 1][c] = -1

        total, waterLevel = 0, 0
        heapq.heapify(boundary)

        while boundary:
            h, r, c = heapq.heappop(boundary)
            waterLevel = max(waterLevel, h)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 < nr < R - 1 and 0 < nc < C - 1 and grid[nr][nc] != -1:
                    total += max(0, waterLevel - grid[nr][nc])
                    heapq.heappush(boundary, (grid[nr][nc], nr, nc))
                    grid[nr][nc] = -1

        return total
