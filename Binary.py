
import collections
import math
from typing import List


class Binary:
    def __init__(self) -> None:
        pass

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = 0
        while left <= right:
            mid = (right-left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return nums[mid]
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, column = len(matrix), len(matrix[0])
        top, bot = 0, rows-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
        if not (top <= bot):
            return False
        row = (top+bot)//2
        l, r = 0, column-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        res = right
        while left < right:
            mid = (left+right)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile/mid))
            if hours > h:
                res = mid
                left = mid+1
            elif hours < h:
                right = mid-1

    def findMin(self, nums: List[int]) -> int:
        res = 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            res = min(nums[left], nums[mid])
            if nums[mid] > nums[left]:
                left += mid+1
            else:
                right += mid-1
        return res

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            # left sorted
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = right - 1
            # right sorted
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid-1
                else:
                    left = left+1
        return -1


if __name__ == "__main__":
    tp = Binary()
    tp.search([5], 5)
