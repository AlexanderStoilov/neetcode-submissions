class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # other approach, using hashset instead, and adding after cleaning, since set = we can only play with 0/1 freqs
        # time: O(n)
        # space: O(n) / O(1) depending on constraints - here only ASCII chars
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

