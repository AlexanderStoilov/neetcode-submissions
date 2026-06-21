class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for ch in t:
            if ch in freq:
                freq[ch] -= 1
            else:
                return False
        for ch in freq:
            if freq[ch] != 0:
                return False
        return True
        