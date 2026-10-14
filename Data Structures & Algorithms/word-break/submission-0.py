class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s.startswith(word, i):
                    if dp(i + len(word)):
                        return True

            memo[i] = False
            return False
        return dp(0)

