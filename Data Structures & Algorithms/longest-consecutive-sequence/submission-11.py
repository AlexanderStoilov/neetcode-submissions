class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        
        max_seq_len = 0
        for num in nums:
            if num-1 not in numset: # start of a sequence
                seq_len = 0
                while num in numset:
                    seq_len += 1
                    num += 1
                max_seq_len = max(max_seq_len, seq_len)
        return max_seq_len
                