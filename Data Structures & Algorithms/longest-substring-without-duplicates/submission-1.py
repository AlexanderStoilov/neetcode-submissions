class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n)
        # space: O(1) - only ASCII chars 
        left = 0
        max_seq = 0
        freq = {}
        for i in range(len(s)):
            char = s[i]
            freq[char] = freq.get(char, 0) + 1
            while freq[char] >= 2:
                freq[s[left]] -= 1
                left += 1
            # at this point, freq[<all elements>] <= 1
            max_seq = max(max_seq, i - left + 1)
        return max_seq

"""
Sliding window with a frequency map.

Expand the window right on each step by including s[i]. If s[i] is already
in the window (freq hits 2), shrink from the left until the duplicate is gone.
After the while loop, [left, i] is guaranteed to contain only unique characters,
so i - left + 1 is a valid candidate for the answer.

time: O(n) — i advances n times, left advances at most n times total across all iterations
space: O(1) — freq holds at most 26 entries (lowercase letters), a fixed constant
"""