class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1
        need_distinct = len(freq_t)
        
        left = 0
        right = -1
        freq_slice = {}
        have_distinct = 0

        min_len = float('inf')
        min_len_borders = [-1, -1]
        
        while right <= len(s) - 2:
            right += 1
            char = s[right]
            if char in freq_slice:
                freq_slice[char] += 1
            else:
                freq_slice[char] = 1
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
        return s[left:right+1]