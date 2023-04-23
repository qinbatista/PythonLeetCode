
import collections
from typing import List


class TwoPointer:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for str in s:
            if str.isalnum():
                newStr += str.lower()
        return newStr == newStr[::-1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict = {}
        for index, number in enumerate(numbers):
            if number in myDict:
                return [myDict[number], index+1]
            else:
                value = target - number
                myDict[value] = index+1
        return []
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        while left<right:
            lowestHeight = min(height[left], height[right])
            res = max((right-left)*lowestHeight,res)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return res

if __name__ == "__main__":
    tp = TwoPointer()
    print(tp.isPalindrome("A man, a plan, a canal: Panama"))
    # print(tp.twoSum([2,3,4], 6))
    # print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
