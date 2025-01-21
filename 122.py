class Solution:
    def maxProfit(self, prices):
        prev = prices[0]
        res = 0

        for price in prices[1:]:
            if price > prev:
                res += price - prev

            prev = price

        return res
