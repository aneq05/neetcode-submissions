class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    elif stack[-1] > abs(asteroid):
                        # 5 -2
                        break
                    else:
                        stack.pop()


            # stack.append(asteroid)
        return stack



# - check the direction (pos or neg val)
# - if they are opposite -> calculate the damage:
#     - the smaller one explodes
#     - same sizes = both explode

# stack:
# 2
# 4
