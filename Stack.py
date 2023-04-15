
import collections
from typing import List


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack == []:
            val = min(value, value)
        else:
            val = min(value, self.minStack[-1])

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    s.top()
    print(s.getMin())
    # print(tp.isPalindrome("0P"))
    # print(tp.twoSum([2,3,4], 6))
    # print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
