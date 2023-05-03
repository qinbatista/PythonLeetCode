
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
        myDic = {}
        for index, number in enumerate(numbers):
            remaining = target - number
            if number in myDic:
                return [myDic[number], index+1]
            else:
                myDic[remaining] = index+1
        return []

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            lowestHeight = min(height[left], height[right])
            res = max((right-left)*lowestHeight, res)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            l = index+1
            r = len(nums)-1
            while l < r:
                threeSum = num + nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


if __name__ == "__main__":
    tp = TwoPointer()
    print(tp.isPalindrome("A man, a plan, a canal: Panama"))
    # print(tp.twoSum([2,3,4], 6))
    # print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
