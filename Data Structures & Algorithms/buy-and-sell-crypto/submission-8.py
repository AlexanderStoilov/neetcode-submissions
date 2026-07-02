class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # same style to textbook solution of "at each step, if we sell there, whats the min (buy) so far -> get max of all options "
        # but inverse - we anchor the buy and look for the max after it
        # time: O(n)
        # space: O(1)
        cur_max = float('-inf')
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            cur_max = max(cur_max, prices[i])
            # if we buy today:
            potential_profit = cur_max - prices[i]
            max_profit = max(max_profit, potential_profit)

        return max_profit