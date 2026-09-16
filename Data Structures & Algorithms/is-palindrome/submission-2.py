class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_s = "".join(ch.lower() for ch in s if ch.isalnum())
        return sanitized_s == sanitized_s[::-1]