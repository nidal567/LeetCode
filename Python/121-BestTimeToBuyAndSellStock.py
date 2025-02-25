class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            current_profit = price - min_price

            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit

        """ Kadane's Algorithm
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > profit:
                profit = prices[i] - buy
        return profit
        """