from heapq import heappop, heappush

class Solution:
    def highestPeak(self, isWater):
        R, C = len(isWater), len(isWater[0])
        res = [[R + C] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if isWater[r][c] == 1:
                    res[r][c] = 0

        for r in range(R):
            for c in range(C):
                if r > 0:  res[r][c] = min(res[r][c], res[r - 1][c] + 1)
                if c > 0:  res[r][c] = min(res[r][c], res[r][c - 1] + 1)
        
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if r < R-1:  res[r][c] = min(res[r][c], res[r + 1][c] + 1)
                if c < C-1:  res[r][c] = min(res[r][c], res[r][c + 1] + 1)

        return res
