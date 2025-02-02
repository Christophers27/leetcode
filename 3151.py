class Solution:
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        
        prev = nums[0] % 2

        for num in nums[1:]:
            if num % 2 == prev:
                return False
            
            prev = num % 2
        
        return True