class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## At each step check: if we bought at cur min (optimal so far) and sell right now, how much profit
        # time: O(n)
        # space: O(1)
        cur_min = float('inf')
        max_profit = float('-inf')
        for i in range(len(prices)):
            if prices[i] < cur_min: # tracking min so far
                cur_min = prices[i]
            cur_profit = prices[i] - cur_min
            max_profit = max(max_profit, cur_profit)
        return max_profit
            