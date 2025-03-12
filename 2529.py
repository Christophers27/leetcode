class Solution:
    def maximumCount(self, nums):
        def binarySearch(target):
            left, right = 0, len(nums) - 1
            res = len(nums)

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    res = mid
                    right = mid - 1

            return res

        neg = binarySearch(0)
        pos = len(nums) - binarySearch(1)

        return max(pos, neg)
