class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_value = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price-best_buy_value)
            best_buy_value = min(best_buy_value, price)
        return max_profit