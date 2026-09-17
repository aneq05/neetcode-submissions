class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(str(d) for d in digits))
        return [int(d) for d in str(number+1)]