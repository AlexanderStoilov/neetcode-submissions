class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        
        max_seq_len = 0
        for num in numset: # important, unique els are visited once => helps T.C.
            if num-1 not in numset: # start of a sequence
                seq_len = 0
                while num in numset:
                    seq_len += 1
                    num += 1 # modifies only the local while loop variable; does not affect nums or the outer loop iteration
                max_seq_len = max(max_seq_len, seq_len)
        return max_seq_len

        # time: O(n)
        # space: O(n)

        """
        Key insight: the while loop's total executions across the ENTIRE run is what matters, not per outer iteration.
        
        Solution 1 - iterate over nums:
          O(n^2) worst case. Duplicates are the killer:
          if num=1 appears 3 times in nums, and the sequence [1,2,3] has length 3,
          the while loop runs 3x3=9 times. k duplicates × L sequence length = k×L per sequence.
        
        Solution 2 - iterate over numset:
          O(n). numset deduplicates, so each unique number triggers the while loop at most once.
          Each number is visited by the while loop at most once total = n times total. O(n).
        
        The "it looks like O(n^2)" trap: nested loops aren't always O(n^2).
        When the inner loop's TOTAL work across all outer iterations is bounded by n
        (either via removal or deduplication), you add instead of multiply: O(n) + O(n) = O(n).
        """               