class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagram_map = {}

        for word in strs:
        
            sorted_word = "".join(sorted(word))
        
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = [word]
            else:
                anagram_map[sorted_word].append(word)

        final_list = []

        for key in anagram_map:
            final_list.append(anagram_map[key])

        return final_list