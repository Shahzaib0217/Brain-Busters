class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_profit = 0
        # using variable sliding window (https://www.geeksforgeeks.org/window-sliding-technique/)
        while r < len(prices):
            profit = prices[r]-prices[l]
            max_profit = max(profit, max_profit) 
            
            # if the profit is -ve move r ahead else move l pointer ahead
            if profit >= 0:
                r+=1
            else:
                l+=1
            
        return max_profit

        