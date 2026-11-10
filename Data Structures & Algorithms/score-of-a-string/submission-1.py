class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(1, len(s)):
            numerical_val = alphabet.index(s[i]) - alphabet.index(s[i-1])
            score += abs(numerical_val)
        return score