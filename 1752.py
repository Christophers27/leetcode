class Solution:
    def check(self, nums):
        if len(nums) == 1:
            return True
        
        notInOrder = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if notInOrder != -1:  return False

                notInOrder = i
        
        if notInOrder != -1:
            if nums[0] < nums[-1]:
                return False
        
        return True