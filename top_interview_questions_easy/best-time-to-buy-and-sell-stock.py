class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000 # 임의의 최저 주식값
        profit = 0 # 수익
        
        for current_price in prices:
            # 현재가격 - 최저값의 값과 수익 값 중 최대값을 수익값으로 보고 swap
            min_price = min(current_price, min_price)
            profit = max(profit, current_price - min_price)
        return profit
            