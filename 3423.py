class Solution:
    def maxAdjacentDistance(self, nums):
        res = 0

        for i in range(len(nums)):
            res = max(res, abs(nums[i - 1] - nums[i]))

        return res
