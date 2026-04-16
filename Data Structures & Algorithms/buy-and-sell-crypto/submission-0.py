class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 2):
            return 0
        left, right, max_profit = 0, 1, 0
        while right < len(prices):
            buy, sell = prices[left], prices[right]
            if buy < sell:
                max_profit = max(max_profit, sell - buy)
            else:
                left = right
            right += 1
        return max_profit