class Solution:
    def canJump(self, nums):
        jump = 0

        for num in nums:
            if jump < 0:
                return False
            
            jump = max(num, jump)
            jump -= 1

        return True
