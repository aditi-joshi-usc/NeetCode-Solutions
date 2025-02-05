class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 Pointer approach
        max_profit =0
        left = 0
        right = 1

        while right < len(prices):
            

            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right+=1            
            
        
        return max_profit

        #Dynamic programming approach

        # max_profit =0
        # min_price = prices[0]

        # for i in range(1, len(prices), 1):
            
        #     max_profit = max(max_profit, prices[i] - min_price)
        #     min_price = min(min_price, prices[i])
        
        # return max_profit


        
