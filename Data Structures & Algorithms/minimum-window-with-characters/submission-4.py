"""
Minimum Window Substring — Thought Process and Solution
--------------------------------------------------------

PROBLEM: find the shortest substring of s that contains every character
of t, including duplicates. Return "" if no such substring exists.


CORE APPROACH: sliding window
-----------------------------
Expand the right boundary to include more characters until the window
satisfies t. Once satisfied, shrink the left boundary to find the
smallest valid window. Record the minimum. Repeat until right exhausts s.

The validity condition: the window satisfies t when every character c in t
appears in the window at least freq_t[c] times.


NAIVE VALIDITY CHECK: O(|t|) per iteration → O(n·|t|) total (TLE)
-------------------------------------------------------------------
The straightforward approach calls a helper tFitsInSlice() that iterates
over every character in freq_t to check if freq_slice satisfies it.
This is O(|t|) per window move, making the total complexity O(n·|t|).
For large inputs this exceeds the time limit.


OPTIMIZED VALIDITY CHECK: O(1) per iteration → O(n) total
-----------------------------------------------------------
Instead of checking all characters in freq_t from scratch on every step,
maintain a running integer counter:

    need_distinct = len(freq_t)   — number of distinct chars t requires;
                                    computed once, never changes
    have_distinct = 0             — number of distinct chars currently
                                    satisfied by the slice window

The validity check becomes simply: have_distinct == need_distinct → O(1)

Maintaining have_distinct in O(1):

EXPANDING (right moves forward, char added to window):
    freq_slice[char] += 1
    if char in freq_t and freq_slice[char] == freq_t[char]:
        have_distinct += 1
    # Only fires when char is needed AND just reached exact satisfaction;
    # Characters not in freq_t never touch have_distinct at all —
    # so no false positives are possible;

SHRINKING (left moves forward, char removed from window):
    freq_slice[char] -= 1
    if char in freq_t and freq_slice[char] == freq_t[char] - 1:
        have_distinct -= 1
    # freq_t[char] - 1 means freq_slice just dropped BELOW the required;
    # count — char was just satisfied, now it isn't;

Both operations are a single comparison → O(1).


COMMON BUG: initializing right = 0 and incrementing it at the start
---------------------------------------------------------------------
If right starts at 0 and is immediately incremented to 1 before processing,
s[0] is never added to freq_slice.


RETURNING THE RESULT:
---------------------
min_len_borders stores [left, right] of the best window found. If min_len
is still float('inf') after the loop, no valid window was ever found and
we return "". Never rely on the default [-1, -1] accidentally producing ""
via Python's slice quirks — be explicit.

time: O(n+m) — O(m) to build freq_t, O(n) for the sliding window pass
               (right makes n moves, left makes at most n moves total)
space: O(k)  — freq_t and freq_slice together hold at most k entries,
               where k = number of unique characters across s and t
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        need_distinct = len(freq_t)
        
        left = 0
        right = -1
        freq_slice = {}
        have_distinct = 0

        min_len = float('inf')
        min_len_borders = [-1, -1]
        
        for right in range(len(s)):
            char = s[right]
            freq_slice[char] = freq_slice.get(char, 0) + 1 # increase slice freq of 'char'
            if char in freq_t and freq_t[char] == freq_slice[char]:
                # 'char' is needed, and it just reached a satisfactory quantity
                have_distinct += 1

            while need_distinct == have_distinct:
                # while 's' slice fits 't', try lowering it, to maybe find even smaller
                if right - left + 1 < min_len:
                    # but first potentially save cur slice length
                    min_len = right - left + 1
                    min_len_borders = [left, right]

                char = s[left]
                freq_slice[char] -= 1
                if char in freq_t and freq_t[char] == freq_slice[char] + 1:
                    # 'char' is needed, and it was just lowered from just enough quantity
                    have_distinct -= 1
                left += 1

        left, right = min_len_borders
        print(f'left = {left}, right = {right}')
        if min_len == float('inf'):
            return "" 
        return s[left:right+1]