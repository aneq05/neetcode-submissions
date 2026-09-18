class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return self.calc_pow(x, n)
        else:
            x = 1 / x
            return self.calc_pow(x, -n)


    def calc_pow(self, x: float, n: int) -> float:
        result = 1
        for power in range(1,n+1):
            result *= x
        return result 