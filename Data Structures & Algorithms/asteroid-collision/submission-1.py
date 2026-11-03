class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:   # ujemna asteroida
                alive = True

                while stack and stack[-1] > 0:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                        alive = False
                        break
                    elif stack[-1] > abs(asteroid):
                        alive = False
                        break
                    else:
                        stack.pop()

                if alive:   # jeśli mamy same ujemny asteroidy
                    stack.append(asteroid)
        return stack
