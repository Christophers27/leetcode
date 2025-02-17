class Solution:
    def maximumSum(self, nums):
        # For pairs of numbers whose digits sum to the same value, find the maximum sum of the pair
        digitSums = {}  # digitSum -> list of numbers

        for num in nums:
            digitSum = sum([int(digit) for digit in str(num)])

            if digitSum not in digitSums:
                digitSums[digitSum] = [num]
            else:
                digitSums[digitSum].append(num)

        res = -1

        for numbers in digitSums.values():
            if len(numbers) > 1:
                res = max(res, sum(sorted(numbers)[-2:]))

        return res
