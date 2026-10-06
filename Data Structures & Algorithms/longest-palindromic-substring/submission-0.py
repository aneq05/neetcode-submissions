class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        if length % 2 == 0:
            r = length // 2
            l = r - 1 
        else:
            center = length // 2
            l = r = center

        while l == r and l+r <= length:
            l -= 1
            r += 1

        return s[l:r+1]