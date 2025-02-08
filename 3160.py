from collections import defaultdict


class Solution:
    def queryResults(self, limit, queries):
        res = []
        ballColors, colorCounts = dict(), defaultdict(int)
        count = 0

        for ball, color in queries:
            if ball in ballColors:
                colorCounts[ballColors[ball]] -= 1
                if colorCounts[ballColors[ball]] == 0:
                    count -= 1

            ballColors[ball] = color
            colorCounts[color] += 1
            if colorCounts[color] == 1:
                count += 1

            res.append(count)

        return res
