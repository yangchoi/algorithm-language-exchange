class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_num = len(prices)
        output = 0
        min_price = sys.maxsize

        for i in range(day_num):
            if prices[i] < min_price:
                min_price = prices[i]
            output = max(output, prices[i] - min_price)
        return output