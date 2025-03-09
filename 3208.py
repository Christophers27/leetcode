class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        res = left = 0

        colors += colors[: k - 1]

        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right - 1]:
                left = right

            if right - left + 1 >= k:
                res += 1

        return res
