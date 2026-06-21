class Solution:
    def is_valid(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # the second "left < right" checks here are cos during skipping bad characters we can go over the 
            #   > in case of left -  the total length
            #   > in case of right - the index 0
            # and this check is more convenient than the left <= len(...)-1 and right >= 0
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True