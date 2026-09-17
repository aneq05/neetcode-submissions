class Solution:
    def isHappy(self, n: int) -> bool:
        # for infinite loop
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True

