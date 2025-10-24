class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pro = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                pro += p
            l = r
            r += 1
        return pro
