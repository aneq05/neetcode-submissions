class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        res = self.recur_pow(x, abs(n))
        return res if n>0 else 1/res


    def recur_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        half = self.recur_pow(x*x, n//2)
        return half*x if n % 2 else half 
