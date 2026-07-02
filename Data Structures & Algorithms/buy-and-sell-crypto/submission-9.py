class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers, from solutions
        # time: O(n)
        # space: O(1)
        l = 0
        r = 1
        max_profit = 0
        while l < r <= len(prices) - 1:
            if prices[r] > prices[l]:
                cur_profit = prices[r] - prices[l]
                max_profit = max(max_profit, cur_profit)
            else:
                l = r
            r += 1
        return max_profit