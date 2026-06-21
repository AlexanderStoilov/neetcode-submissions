class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hat, [act, cat], [stop, posts, tops] -> 
        # 1      2    2       3     3     3

        # {'h': 1, 'a': 1, 't': 1} -> 1
        # {'a': 1, 'c': 1, 't': 1} -> 2
        # {'s': 1, 't': 1, 'o': 1, 'p': 1} -> 3
        
        # {map1: 1, map2: }

        groups = {} # frequency map: words

        for word in strs:
            word_freq = {}
            for c in word:
                word_freq[c] = word_freq.get(c, 0) + 1
            
            ## sorting is O(m log m), where m = unique characters in word
            # but since m <= 26, it is effectively O(1)
            
            ## tuple is needed cos dictionary can have only immutable object as key (lists, dicts are mutable) 
            word_freq_tuple = tuple(sorted(word_freq.items()))
            if word_freq_tuple in groups:
                groups[word_freq_tuple].append(word)
            else:
                groups[word_freq_tuple] = [word]

        print(f"groups = {groups}")
        res = []
        for word_group in groups.values():
            res.append(word_group)

        return res     

    # n = number of words
    # k = avg number of characters in word
    # time: O(n.k)
    # space:
    #   including output: O(n.k)
    #   auxiliary: O(n)
