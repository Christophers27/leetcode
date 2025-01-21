class Solution:
    def firstCompleteIndex(self, arr, mat):
        loc = dict()  # Key is num, value is tuple of (row, col)
        R, C = len(mat), len(mat[0])
        rows = [0] * R  # Num of painted cells in said row. Filled when val is C
        cols = [0] * C  # Same

        # Build loc
        for i in range(R):
            for j in range(C):
                loc[mat[i][j]] = (i, j)

        # Go through list
        for i, num in enumerate(arr):
            r, c = loc[num]
            rows[r] += 1
            if rows[r] == C:
                return i
            cols[c] += 1
            if cols[c] == R:
                return i
