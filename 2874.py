class Solution(object):
    def maximumTripletValue(self, nums):
        N = len(nums)
        maxSeenFromLeft = [nums[0]] * N

        for i in range(1, N):
            maxSeenFromLeft[i] = max(maxSeenFromLeft[i - 1], nums[i])

        res = 0
        maxSeenFromRight = nums[-1]

        for i in range(1, N - 1)[::-1]:
            res = max(res, (maxSeenFromLeft[i - 1] - nums[i]) * maxSeenFromRight)
            maxSeenFromRight = max(maxSeenFromRight, nums[i])

        return res
