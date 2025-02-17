class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        N = len(part)

        for c in s:
            res.append(c)

            if c == part[-1] and "".join(res[-N:]) == part:
                res[-N:] = []

        return "".join(res)
