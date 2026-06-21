class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # chars = {_: 0 for _ in range(ord('z')-ord('a'))}
        chars = [0] * 26
        for i in range(len(s)):
            chars[ord(s[i])-ord('a')] += 1
            chars[ord(t[i])-ord('a')] -= 1
        
        for val in chars:
            if val != 0:
                return False
        return True