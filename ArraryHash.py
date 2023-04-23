
import collections
from typing import List


class ArrayHash:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            else:
                hash.add(num)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for index in range(len(s)):
            s_dic[s[index]] = s_dic.get(s[index], 0)+1
            t_dic[t[index]] = t_dic.get(t[index], 0)+1
        return s_dic == t_dic

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueDic = {}
        for index, num in enumerate(nums):
            remaining_value = target - num
            if remaining_value in valueDic:
                return [valueDic[remaining_value], index]
            else:
                valueDic[num] = index
        return []

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()  # type: ignore

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore
        # count each values
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        # list all possible count, the max size is the length of the nums
        freq = [[] for i in range(len(nums))]
        for key, value in count.items():
            freq[value] = key

        # find the most frequency k, index from last to start, as long as the length is equal to k, we find the value
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if (len(res)) == k:
                    return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # calculate the prefix, prefix means previous values's multiple
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # calculate the postfix, postfix means values behind the values' multiple
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[r] or board[r][c] in square[(r//3, c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True

    def encode(self, strs):
        res = ""
        for s in strs:
            res = res + str(len(s))+"#"+s
        return res

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j+1+length
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    arrayHash = ArrayHash()
    # arrayHash.longestConsecutive([100, 4, 200, 1, 3, 2])
    # print(arrayHash.decode(arrayHash.encode(["lint", "code", "love", "you"])))
    # print(arrayHash.containsDuplicate([1, 2, 3, 1]))
    # print(arrayHash.isAnagram("anagram", "nagaram"))
    # print(arrayHash.twoSum([2, 7, 11, 15], 9))
    # print(arrayHash.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(arrayHash.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    # print(arrayHash.productExceptSelf([1, 2, 3, 4]))
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # print(arrayHash.isValidSudoku(board))
