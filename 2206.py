class Solution:
    def maximumCandies(self, candies, k):
        def check(c):
            if c == 0:
                return False

            total = 0
            for pile in candies:
                total += pile // c
            return total >= k

        left = 0
        right = max(candies)

        while left < right:
            mid = (left + right) // 2 + 1

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
