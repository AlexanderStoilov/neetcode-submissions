class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n)
        # space: O(1)
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
