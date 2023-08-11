from typing import List

class MinStack:

    def __init__(self):
        self.list = []
        self.length = 0
        self.min = []


    def push(self, val: int) -> None:
        if self.length == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        self.length += 1
        self.list.append(val)


    def pop(self) -> None:
        if self.list[-1] == self.min[-1]:
            self.min.pop()
        self.list.pop()
        self.length -= 1


    def top(self) -> int:
        return self.list[-1]


    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
