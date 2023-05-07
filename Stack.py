
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
        for value in tokens:
            if value == "+":
                stack.append(int(stack.pop()+stack.pop()))
            elif value == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b-a))
            elif value == "*":
                stack.append(int(stack.pop()*stack.pop()))
            elif value == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(value))
        return stack[-1]

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backTrack(open+1, close)
                stack.pop()
            if open > close:
                stack.append(")")
                backTrack(open, close+1)
                stack.pop()
        backTrack(0, 0)
        return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, s_index = stack.pop()
                res[s_index] = index-s_index
            stack.append([temp, index])
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
        if len(s) == 1:
            return False

        dic = {")": "(",
               "]": "[",
               "}": "{"}
        stack = []
        for _str in s:
            if _str not in dic:
                stack.append(_str)
            else:
                if len(stack) != 0:
                    if stack[-1] in dic[_str]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return stack == []


if __name__ == "__main__":
    s = Stack()
    # print(s.isValid("(])"))
    # s.push(-2)
    # s.push(0)
    # s.push(-3)
    # print(s.getMin())
    # s.pop()
    # s.top()
    # print(s.getMin())
    # print(s.evalRPN(["2", "1", "+", "3", "*"]))
    # print(s.generateParenthesis(3))
    # print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
