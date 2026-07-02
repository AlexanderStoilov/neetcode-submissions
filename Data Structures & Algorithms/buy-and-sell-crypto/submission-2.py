class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Kadane
        # time: O(n)
        # space: O(1)

        diffs = []
        for i in range(1, len(prices)):
            diffs.append(prices[i] - prices[i - 1])
        # now find longest consecutive "subarray" (really - subsequence)

        max_seq = 0
        cur_seq = 0
        for num in diffs:
            cur_seq += num
            # if better to start over, do it
            if cur_seq < 0:
                cur_seq = 0
            max_seq = max(max_seq, cur_seq)
        return max_seq

