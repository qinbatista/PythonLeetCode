
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
        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a)+int(b))
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b)-int(a))
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a)*int(b))
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b)/int(a))
            else:
                stack.append(token)
        return stack[-1]

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backTrack(openN+1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(")")
                backTrack(openN, closedN+1)
                stack.pop()
        backTrack(0, 0)
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperature>stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = index -stackIndex
            stack.append((temperature,index))
        return res

    def carFleet(self, target: int, position: List[int], speed: list[int]) -> int:
        pair = [[_position, _speed] for _position, _speed in zip(position, speed)]
        stack = []
        pair = sorted(pair)[::-1]
        for carInfo in pair:
            stack.append((target - carInfo[0])/carInfo[1])
            if len(stack) > 2 and stack[-2] >= stack[-1]:
                stack.pop
        return len(stack)

    def isValid(self, s: str) -> bool:
        closeSymbleDic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if stack and stack[-1] == closeSymbleDic[char]:
                stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Stack()
    # print(s.isValid("()"))
    # s.push(-2)
    # s.push(0)
    # s.push(-3)
    # print(s.getMin())
    # s.pop()
    # s.top()
    # print(s.getMin())
    # print(s.evalRPN(["2", "1", "+", "3", "*"]))
    # print(s.generateParenthesis(3))
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
