from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums):
        products = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]] += 1

        res = 0

        for n in products.values():
            res += 8 * (n * (n - 1) / 2)

        return int(res)
