class Solution:
    def minCapability(self, nums, k):
        N = len(nums)

        def check(capability):
            count = i = 0
            while i < N:
                if nums[i] <= capability:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        left, right = min(nums), max(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
