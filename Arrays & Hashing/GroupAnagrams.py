class Solution:
    def groupAnagrams(self, strs):
        # Dictionary with list as default value for a key
        anagram_map = defaultdict(list)
        
        for word in strs:
            # sorted() returns an array of characters. So its necessary to join them here
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())