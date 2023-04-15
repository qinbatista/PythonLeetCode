
import collections
from typing import List


class TwoPointer:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        leftPoint = 0
        rightPoint = len(s)-1
        try:
            while leftPoint < rightPoint:
                while (s[leftPoint] >= 'a' and s[leftPoint] <= 'z') == False and (s[leftPoint] >= '0' and s[leftPoint] <= '9') == False:
                    leftPoint = leftPoint+1
                while (s[rightPoint] >= 'a' and s[rightPoint] <= 'z') == False and (s[rightPoint] >= '0' and s[rightPoint] <= '9') == False:
                    rightPoint = rightPoint-1
                if s[leftPoint] != s[rightPoint]:
                    return False
                leftPoint = leftPoint+1
                rightPoint = rightPoint-1
            return True
        except Exception as e:
            return True

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict = {}
        for index, number in enumerate(numbers):
            if number in myDict:
                return [myDict[number], index+1]
            else:
                value = target - number
                myDict[value] = index+1
        return []


if __name__ == "__main__":
    tp = TwoPointer()
    # print(tp.isPalindrome("0P"))
    print(tp.twoSum([2,3,4], 6))
