
import collections
from typing import List


class Binary:
    def __init__(self) -> None:
        pass

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid+1
            else:
                return mid
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


if __name__ == "__main__":
    tp = Binary()
