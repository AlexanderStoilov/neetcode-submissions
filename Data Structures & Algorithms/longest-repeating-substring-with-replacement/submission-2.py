class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # time: O(n) | left could make at most n moves, right will make n moves => <= 2n
        # space: O(n)
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
                max_len = max(max_len, (right - left + 1))
            else:
                # max_freq could be stale, but it's still ok?
                while max_freq < (right - left + 1) - k:
                    freq[s[left]] -= 1
                    left += 1
            right += 1
        return max_len
            
