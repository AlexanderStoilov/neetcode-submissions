class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = []
        for c in s:
            if c.isalnum():
                s_clean.append(c.lower())
        for i in range(len(s_clean) // 2):
            if s_clean[i] != s_clean[len(s_clean)-i-1]:
                return False
        return True