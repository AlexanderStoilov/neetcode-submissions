class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # time: O(n) | left could make at most n moves, right will make n moves => <= 2n
        # space: O(n) / O(1) - ascii limitation
        left = 0
        freq = {}
        max_freq = 0
        max_len = 0
        right = 0
        while right <= len(s) - 1:
            # increase freq of cur char
            freq[s[right]] = freq.get(s[right], 0) + 1

            # potenitally update max freq
            max_freq = max(max_freq, freq[s[right]])

            if max_freq >= (right - left + 1) - k:
                # valid range, satisfying the property of "with <= k replacements there can be only 1 distinct character"
                # so we save its len and potentially update max_len
                max_len = max(max_len, (right - left + 1))
            else:
                # substring too long, need to shorten
                # max_freq could be stale, but it's still ok
                freq[s[left]] -= 1
                left += 1
            right += 1
        return max_len
            

"""
Longest Repeating Character Replacement — Thought Process
----------------------------------------------------------

PROBLEM: given string s and integer k, find the length of the longest substring
where you can replace at most k characters to make all characters the same.


APPROACH 1 (FAILED): two pointers from both ends
-------------------------------------------------
First instinct was to anchor on the most frequent character in the entire string,
then use left and right pointers closing in from both ends, always moving the
pointer whose end doesn't contain the top element.

Why it fails: the optimal window could start and end anywhere in the string.
When we move a pointer inward, we might be discarding the very characters that
form the optimal window on the other side. There's no way to know which end to
shrink without already knowing the answer. Example: "ABAA" k=0 — the answer is
"AA" at the end, but closing from the left destroys it before we ever see it.


APPROACH 2 (FAILED): sliding window tracking top_el by name
------------------------------------------------------------
Correct direction — expand right, shrink left when invalid. The validity
condition for a window [left, right] is:

    (window length) - (frequency of most common char in window) <= k

In other words: the number of characters we'd need to replace equals the
window length minus however many characters we DON'T need to replace (the
most frequent ones). If that count exceeds k, the window is invalid.

Tracked top_el by name (the actual character that is most frequent). The
problem: when shrinking from the left, we might remove the top element from
the window, and finding the new top element requires scanning all of freq —
and worse, the logic for when to update top_el mid-shrink is tangled and
error-prone. Multiple bugs emerged that were hard to reason about cleanly.


APPROACH 3 (CORRECT): sliding window tracking max_freq as a number
-------------------------------------------------------------------
Key insight: we never actually need to know *which* character is most frequent
— we only ever use its frequency count as a number. So instead of tracking
top_el by name and looking up freq[top_el], we just track max_freq directly:
a single integer representing the highest frequency any character has achieved
in any window seen so far.

Updating max_freq on expansion is O(1): max_freq = max(max_freq, freq[s[right]])

The subtle part — why max_freq being "stale" is safe:
When we shrink from the left and remove the top element, max_freq might
become an overestimate of the true current maximum frequency. You might
expect this to cause incorrect results. It doesn't, for this reason:

The window only ever grows when max_freq genuinely increases — i.e. when we
find a character that is more frequent than anything seen before. In that case
the growth is legitimate and max_len correctly records it.

When max_freq is stale (overestimating), the validity condition
    max_freq >= (right - left + 1) - k
fails when right advances, so we shrink left by 1. Net result: the window
slides forward at the same size — it never grows on a stale max_freq.

So the window size at any point equals at most the largest genuinely valid
window seen so far. A stale max_freq never causes the window to grow beyond
what is actually achievable, so max_len is always correct.

Because the window only grows or stays the same (never shrinks net), the
else branch always moves left by exactly 1 — it's a single if, not a while.

time: O(n) — right makes n moves, left makes at most n moves total
space: O(1) — freq holds at most 26 entries (uppercase English letters)
"""