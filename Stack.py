
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

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for str in tokens:
            if str == "+":
                stack.append(stack.pop()+stack.pop())
            elif str == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif str == "*":
                stack.append(stack.pop()*stack.pop())
            elif str == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(str))
        return stack[-1]

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    s = Stack()
    # s.push(-2)
    # s.push(0)
    # s.push(-3)
    # print(s.getMin())
    # s.pop()
    # s.top()
    # print(s.getMin())
    # print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.generateParenthesis(3))
