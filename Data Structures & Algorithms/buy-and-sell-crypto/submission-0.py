class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        maxprofit = 0
        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit, profit)
            else:
                # cheaper buying day
                l = r
            r += 1
        return maxprofit


            

        