class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = Counter(t)

        for character in s:
            counter[character] -= 1
        
        for char in counter:
            if counter[char] == 1:
                return char