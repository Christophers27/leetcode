class Solution:
    def rotate(self, nums, k):
        nums.reverse()
        k = k % len(nums)
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
