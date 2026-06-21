class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stripped = ""
        for char in s:
            if char.isalnum(): # is alphanumeric, short form for the is_valid in sol 1
                # this inflates complexity to O(k^2) where k=len(s)
                s_stripped += char.lower()

        # same idea: return s_stripped == s_stripped[::-1]
        for i in range(len(s_stripped)): # not optimal to compare each pair twice (iterating the whole array)
            if s_stripped[i] != s_stripped[len(s_stripped)-i-1]:
                return False
        return True
