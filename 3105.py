class Solution:
    def longestMonotonicSubarray(self, nums):
        if len(nums) == 1:
            return 1

        cur, res = 1, 1
        direction = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if direction == 1:
                    cur += 1
                elif direction == 0:
                    cur = 2
                    direction = 1
                else:
                    res = max(res, cur)
                    cur = 2
                    direction = 1
            elif nums[i] == nums[i - 1]:
                res = max(res, cur)
                cur = 1
                direction = 0
            else:
                if direction == 1:
                    res = max(res, cur)
                    cur = 2
                    direction = -1
                elif direction == 0:
                    cur = 2
                    direction = -1
                else:
                    cur += 1

        res = max(res, cur)

        return res
