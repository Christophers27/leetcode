class Solution:
    def checkPowersOfThree(self, n):
        for exp in range(15, -1, -1):
            if n >= 3**exp:
                n -= 3**exp

            if n == 0:
                return True

        return False
