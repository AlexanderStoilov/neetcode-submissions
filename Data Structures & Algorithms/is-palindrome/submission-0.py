class Solution:
    def is_valid(self, char: str) -> bool:
        return (ord(char) >= ord('a') and ord(char) <= ord('z')) \
        or (ord(char) >= ord('A') and ord(char) <= ord('Z')) \
        or (ord(char) >= ord('0') and ord(char) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.is_valid(s[left]):
                left += 1
                continue
            if not self.is_valid(s[right]):
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True