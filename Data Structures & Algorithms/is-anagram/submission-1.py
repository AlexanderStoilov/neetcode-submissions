class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int) # default = 0 (calls int() -> 0, optimized in C)
        t_freq = defaultdict(lambda: 0) # default = 0 (calls Python lambda, slightly slower)
        for chr in s:
            s_freq[chr] += 1
        for chr in t:
            t_freq[chr] += 1
        
        for chr in s_freq:
            if s_freq[chr] != t_freq.get(chr, 0):
                return False

        return len(s_freq) == len(t_freq)
        

# getordefault(<key>, <return def value if key not present>)