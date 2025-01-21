class Solution:
    def maxProfit(self, prices):
        lowest = prices[0]
        res = 0

        for price in prices[1:]:
            if price < lowest:
                lowest = price
            else:
                res = max(res, price - lowest)

        return res
