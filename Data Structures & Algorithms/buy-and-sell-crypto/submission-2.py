class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = None
        for num in prices:
            # update minimum if we see a lower price
            if minimum is None or num < minimum:
                minimum = num
            else:
                # calculate profit only if we sell after buying
                profit = max(profit, num - minimum)
        return profit
        