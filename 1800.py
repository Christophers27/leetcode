class Solution:
    def maxAscendingSum(self, nums):
        if len(nums) == 1:
            return nums[0]

        res = 0
        cur = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                res = max(res, cur)
                cur = nums[i]
        
        res = max(res, cur)
        return res