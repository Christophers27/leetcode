class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subbox = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                el = board[r][c]

                if el == ".":
                    continue

                # Check rows
                if el in rows[r]:
                    return False
                rows[r].add(el)

                # Check cols
                if el in cols[c]:
                    return False
                cols[c].add(el)

                # Check sub-boxes
                if el in subbox[(r // 3) * 3 + (c // 3)]:
                    return False
                subbox[(r // 3) * 3 + (c // 3)].add(el)

        return True
