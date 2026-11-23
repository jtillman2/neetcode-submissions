class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for word in strs:
            encodeString += str(len(word)) + "#" + word
        return encodeString


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            # read the length (could be multiple digits) up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])      # digits from i to j-1
            start = j + 1             # first char of the word
            end = start + length      # exclusive
            res.append(s[start:end])  # word is s[start:end]
            i = end                   # jump to next length
        return res
                

