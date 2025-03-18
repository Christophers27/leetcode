class Solution:
    def longestNiceSubarray(self, nums):
        N = len(nums)
        res = 1
        left = 0
        curBits = 0

        for right in range(N):
            while curBits & nums[right] != 0:
                curBits ^= nums[left]
                left += 1

            curBits |= nums[right]

            res = max(res, right - left + 1)

        return res
