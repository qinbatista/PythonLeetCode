
import collections
from typing import List


class TwoPointer:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        if newStr == newStr[::-1]:
            return True
        return False

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        for i in range(len(numbers)):
            if target < numbers[left]+numbers[right]:
                right -= 1
            elif target < numbers[left]+numbers[right]:
                left += 1
            else:
                return [left+1, right+1]

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            if height[left] > height[right]:
                maxArea = max(maxArea, height[right]*(right-left))
            else:
                maxArea = max(maxArea, height[left]*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            l = index + 1
            r = len(nums)-1
            while l < r:
                threeSum = num+nums[l]+nums[r]
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
    # print(tp.isPalindrome("A man, a plan, a canal: Panama"))
    # print(tp.twoSum([2,3,4], 6))
    print(tp.maxArea([1,8,6,2,5,4,8,3,7]))
