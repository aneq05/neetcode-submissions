class Solution:
    def numDecodings(self, s: str) -> int:
        # przechodzimy po znakach w s:
        # dwie operacje - chr i ord -> numer na znak -> to finalnie niepotrzebne bo wystarczy zliczyć ilość sposobów zdekodowania a nie realnie dekodować 
        # 1) bierzemy oba znaki jeśli są mniejsze lub równe 26 -> czyli mieszczą się w alfabecie 
        # 1a) tutaj też nie możemy mieć po wybraniu dwóch znaków 0 z przodu
        # 2) bierzemy pojedyncze znaki -> jeśli nie są zerami 
        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            # 1 char
            ways = dp(i+1)
            # 2 chars
            if i + 1 < len(s) and 10 <= int(s[i:i+2])<= 26:
                ways += dp(i+2)

            return ways
        return dp(0)