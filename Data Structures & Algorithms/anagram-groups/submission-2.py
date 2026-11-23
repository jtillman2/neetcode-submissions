class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for words in strs:
            count = [0] * 26 #build frequency count
            for char in words:
                position = ord(char) - ord('a') #gives you the postion of the letter in the alphabet with a = 0, b = 1 ...
                count[position] += 1
            
            wordFreq = tuple(count)

            if wordFreq in groups:
                groups[wordFreq] = groups[wordFreq] + [words]
            else:
                groups[wordFreq] = [words]
        return list(groups.values())
        