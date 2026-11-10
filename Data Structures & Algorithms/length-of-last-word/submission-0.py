class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_count = 0

        for index in range(len(s) - 1, -1, -1):
            if s[index] != ' ':
                letter_count += 1
            else:
                if letter_count > 0:
                    break
                continue
        return letter_count