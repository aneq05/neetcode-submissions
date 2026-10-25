class MyStack:

    def __init__(self):
        self.first_queue = deque()
        self.second_queue = deque()

    def push(self, x: int) -> None:
        self.second_queue.append(x)
        while self.first_queue:
            self.second_queue.append(self.first_queue.popleft())

        self.first_queue, self.second_queue = self.second_queue, self.first_queue

    def pop(self) -> int:
        return self.first_queue.popleft()

    def top(self) -> int:
        return self.first_queue[0]

    def empty(self) -> bool:
        return len(self.first_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()