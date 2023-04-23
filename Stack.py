
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

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i-stackIndex)
            stack.append([t, i])
        return res

    def carFleet(self, target: int, position: List[int], speed:list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

    def isValid(self, s: str) -> bool:
        if len(s)==1:return False

        dic = {")":"(",
               "]":"[",
               "}":"{"}
        stack = []
        for _str in s:
            if _str not in dic:
                stack.append(_str)
            else:
                if len(stack)!=0:
                    if stack[-1] in dic[_str]:
                         stack.pop()
                    else:
                        return False
                else:
                        return False
        return stack==[]





if __name__ == "__main__":
    s = Stack()
    print(s.isValid("(])"))
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
    # print(s.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
