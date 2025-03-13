class Solution:
    def minZeroArray(self, nums, queries):
        N = len(nums)

        def check(k):
            diffArr = [0] * (N + 1)

            for i in range(k):
                left, right, val = queries[i]
                diffArr[left] += val
                diffArr[right + 1] -= val

            total = 0
            for i in range(N):
                total += diffArr[i]
                if total < nums[i]:
                    return False

            return True

        left, right = 0, len(queries)

        if not check(right):
            return -1

        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
