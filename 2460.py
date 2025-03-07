class Solution:
    def applyOperations(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        point1, point2 = 0, 0

        while point2 != len(nums):
            if nums[point2] != 0:
                temp = nums[point1]
                nums[point1] = nums[point2]
                nums[point2] = temp
                point1 += 1
            point2 += 1

        return nums
