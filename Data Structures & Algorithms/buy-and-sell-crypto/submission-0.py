class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_value = min(prices)
        best_sell_value = max(prices)

        if prices.index(best_buy_value) == len(prices) - 1:
            return 0
        else:
            max_diff = 0
            for price in range(prices.index(best_buy_value)+1,len(prices) - 1):
                if price - best_buy_value > max_diff:
                    max_diff = price
                best_sell_value = prices[price]

        return best_sell_value - best_buy_value