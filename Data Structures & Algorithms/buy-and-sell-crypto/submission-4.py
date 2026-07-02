class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Kadane
        # time: O(n)
        # space: O(n)

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

"""
Kadane's algorithm applied to the daily price differences array.

Key insight: the profit from buying on day i and selling on day j equals the sum
of all daily changes between those two days — diffs[i+1] + diffs[i+2] + ... + diffs[j]
— because the intermediate prices telescope and cancel, leaving just prices[j] - prices[i].
So maximum profit = maximum subarray sum of the diffs array, which is exactly what
Kadane's algorithm solves.

Kadane's algorithm requires two separate variables serving two separate purposes:
    cur_seq — the running sum of the current subarray candidate. Gets reset to 0
              whenever it goes negative, because a negative running sum means we're
              better off starting a fresh subarray from the next element than
              extending the current one.
    max_seq — the global best cur_seq has ever reached. Only ever increases, never
              resets. Just passively observes cur_seq and records its peak.

These two variables cannot be merged into one. cur_seq needs to reset aggressively
to implement the "start fresh" decision. max_seq needs to never reset in order to
remember the best answer seen so far. Trying to use one variable for both purposes
simultaneously destroys both pieces of information — the running sum gets polluted
by the global best, and the global best gets dragged down by resets. Two separate
concerns require two separate variables.

The diffs array can be eliminated by computing prices[i] - prices[i-1] inline,
keeping space at O(1). Alternatively, the min-so-far approach solves the same
problem more directly by tracking the cheapest buy price seen up to each day and
checking if selling today beats the current best profit — same complexity, different
framing. The Kadane's framing generalizes more naturally to variants of this problem
involving multiple transactions, cooldown periods, or transaction fees.

time: O(n) — single pass through diffs (or prices inline)
space: O(n) — for the diffs array; O(1) if diffs computed inline
"""

