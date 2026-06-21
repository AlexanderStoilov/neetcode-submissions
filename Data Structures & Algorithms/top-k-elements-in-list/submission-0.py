class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force: freq dictionary, sort by values (n.logn), select top X pairs

        freq = defaultdict(int) # or "lambda: 0". The int() function is faster and initializes to 0
        for num in nums:
            freq[num] += 1
        freq_sorted_by_vals = dict(sorted(freq.items(), key = lambda pair: pair[1], reverse=True))
        freq_list = list(freq_sorted_by_vals.items())

        res = []
        for i in range(k):
            res.append(freq_list[i][0]) # key of i-th position = the num
        return res

    # time: O(n.logn) - sorting
    # space: O(n)
    ## n = len(nums)

