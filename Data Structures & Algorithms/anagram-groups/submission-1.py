class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freq = [0] * 26 # using frequency array instead of dictionary - we can do that
            # since we know the needed size. And it helps, cos we do not have to sort the tuple afterwards 
            for char in word:
                freq[ord(char)-ord('a')] += 1
            freq_key = tuple(freq)
            if freq_key in groups:
                groups[freq_key].append(word)
            else:
                groups[freq_key] = [word]
        
        # anagram_groups = []
        # for word_group in groups.values():
            # anagram_groups.append(word_group)
        # return anagram_groups
        return list(groups.values())


        # k = avg number of characters in a word
        # n = number of words ("strs")
        # time: O(n.k)
        # space: O()