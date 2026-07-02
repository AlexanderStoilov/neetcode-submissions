class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # even more optimal sliding window, from solutions
        # Remember where each character was last seen. If it appears again, move the left pointer after it.
        # and using the last_pos[s[right]] "?exists" and "?is after left" checks, we dont need seen set
        # time: O(n)
        # space: O(n) / O(1) considering ASCII constraint
        left = 0
        last_pos = {}
        max_len = 0
        for right in range(len(s)):
            if s[right] in last_pos and last_pos[s[right]] >= left:
                left = last_pos[s[right]] + 1
            last_pos[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len