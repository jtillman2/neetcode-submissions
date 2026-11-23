class Solution:
    def isPalindrome(self, s: str) -> bool:
        forwardString = ""
        punctuation = "!@#$%^&*(),.?';:[]{}|_+=~`></"
        for letter in s:
            if letter != ' ' and letter not in punctuation:
                forwardString += letter
        return forwardString.lower() == forwardString[::-1].lower()
        