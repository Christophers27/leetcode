class Solution:
    def majorityElement(self, nums):
        res = nums[0]
        count = 1

        for num in nums[1:]:
            if num == res:
                count += 1
            elif count == 0:
                res = num
                count = 1
            else:
                count -= 1

        return res
