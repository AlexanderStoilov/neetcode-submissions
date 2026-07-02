class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # even more optimal sliding window, from solutions
        # Remember where each character was last seen. If it appears again, move the left pointer after it.
        # time: O(n)
        # space: O(n) / O(1) considering ASCII constraint
        left = 0
        last_pos = {}
        seen = set()
        max_len = 0
        for right in range(len(s)):
            if s[right] in seen and last_pos[s[right]] >= left:
                left = last_pos[s[right]] + 1
            else: # technically don't need 'else', since set will take care of duplicate vals and we accounted for them 
                seen.add(s[right])
            last_pos[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len