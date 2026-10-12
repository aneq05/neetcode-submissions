class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []

        for i, char in enumerate(s):
            if char == "(":
                opens.append(i)

            elif char == "*":
                stars.append(i)

            else:  # char == ")"
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while opens and stars:
            if opens[-1] > stars[-1]:
                return False

            opens.pop()
            stars.pop()

        return len(opens) == 0
        