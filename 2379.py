class Solution:
    def minimumRecolors(self, blocks, k):
        window = 0

        for i in range(k):
            if blocks[i] == "W":
                window += 1

        res = window

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                window -= 1

            if blocks[i] == "W":
                window += 1

            res = min(res, window)

        return res
