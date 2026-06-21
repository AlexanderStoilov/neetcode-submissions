class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for chr in s:
            if chr not in s_freq:
                s_freq[chr] = 1
            else:
                s_freq[chr] += 1
        for chr in t:
            if chr not in t_freq:
                t_freq[chr] = 1
            else:
                t_freq[chr] += 1
        
        for chr in s_freq:
            if chr not in t_freq or s_freq[chr] != t_freq[chr]:
                return False

        return len(s_freq) == len(t_freq)
        