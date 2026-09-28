class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = Counter(t)
        window = Counter()

        left = 0
        best_left = 0
        best_len = float("inf")

        def valid():
            for char in need:
                if window[char] < need[char]:
                    return False
            return True

        for right in range(len(s)):
            window[s[right]] += 1

            while valid():
                if right-left+1 < best_len:
                    best_len = right-left+1
                    best_left = left

                window[s[left]] -= 1
                left += 1
            
        if best_len == float("inf"):
            return ""

        return s[best_left:best_left+best_len]