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

"""
Optimized sliding window using last-seen positions.

Instead of shrinking left one step at a time when a duplicate is found,
we jump left directly to last_pos[s[right]] + 1 — skipping past the
previous occurrence of the duplicate in one O(1) move rather than
crawling there one character at a time via a while loop.

The >= left guard is critical: if the last occurrence of s[right] is
already behind the left boundary, it's outside the current window and
isn't actually a duplicate within it — so we must not move left at all.
Without this guard, left could jump backwards, which would incorrectly
shrink the window and produce wrong answers (e.g. 'abba': when right
lands on the final 'a', its last_pos is 0, which is already behind left=2,
so we correctly ignore it).

time: O(n) — right advances n times, left jumps forward (never backward)
space: O(1) — last_pos holds at most one entry per unique character,
                bounded by the character set size, a fixed constant
"""