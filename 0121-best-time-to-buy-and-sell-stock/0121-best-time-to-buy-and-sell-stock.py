class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices)+1)
        cur_price = prices[0]
        max_price = 0
        for idx, price in enumerate(prices):
            if cur_price > price:
                cur_price = price
            else:
                max_price = max(max_price, price - cur_price )
        return max_price