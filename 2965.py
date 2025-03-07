class Solution:
    def findMissingAndRepeatedValues(self, grid):
        N = len(grid)
        counter = [0] * (N * N)
        ans = [0, 0]

        for row in grid:
            for el in row:
                counter[el - 1] += 1

        for num, count in enumerate(counter):
            if count == 2:
                ans[0] = num + 1
            elif count == 0:
                ans[1] = num + 1

        return ans
