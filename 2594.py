class Solution:
    def repairCars(self, ranks, cars):
        left = 0
        right = max(ranks) * (cars**2)

        def check(maxTime):
            count = 0

            for rank in ranks:
                count += int((maxTime / rank) ** 0.5)

            return count >= cars

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
