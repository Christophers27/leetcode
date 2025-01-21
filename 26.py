class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1

        pointer = 1

        for num in nums[1:]:
            if num == nums[pointer - 1]:
                pass
            else:
                nums[pointer] = num
                pointer += 1

        return pointer
