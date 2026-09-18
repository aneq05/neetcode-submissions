class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        prod = 1
        for i in range(abs(n)):
            prod *= x
        
        return prod if n > 0 else 1/prod