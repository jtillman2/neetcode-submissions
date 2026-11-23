class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_mapS = {}
        letter_mapT = {}
        for letter in s:
            if letter not in letter_mapS:
                letter_mapS[letter] = 1
            else:
                letter_mapS[letter] += 1
        for letter in t :
            if letter not in letter_mapT:
                letter_mapT[letter] = 1
            else:
                letter_mapT[letter] += 1
        
        return letter_mapT == letter_mapS
                
        
        