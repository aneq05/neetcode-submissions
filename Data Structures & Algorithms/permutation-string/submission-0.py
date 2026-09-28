class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        left = 0

        for right in range(len(s2)):
            window[s2[right]] += 1

            if right-left+1 > k:
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            if right-left+1 == k:
                if need == window:
                    return True

        return False
                