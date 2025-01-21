class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)

        lastSeen = nums[1]
        pointer = 2

        for num in nums[2:]:
            if num != lastSeen:
                nums[pointer] = num
                lastSeen = num
                pointer += 1
            elif nums[pointer - 2] != num:
                nums[pointer] = num
                pointer += 1
            else:
                pass

        return pointer
