
import collections
from typing import List


class ArrayHash:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _hash = set()
        for num in nums:
            if num in _hash:
                return True
            else:
                _hash.add(num)
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            s_dic[s[i]] = 1+s_dic.get(s[i], 0)
            t_dic[t[i]] = 1 + t_dic.get(t[i], 0)
        return s_dic == t_dic

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dic = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in value_dic:
                return [value_dic[remaining], i]
            value_dic[num] = i

    def groupAnagrams(self, strs: List[str]):
        dic = collections.defaultdict(list)
        for str in strs:
            numList = [0]*26
            for c in str:
                numList[ord(c)-ord("a")] = 1
            dic[tuple(numList)].append(str)
        result = []
        for listValue in dic:
            result.append(dic[listValue])
        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore
        dic = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        for value in dic:
            freq[dic[value]] = value
        result = []
        for i in range(len(freq)-1, 0, -1):
            if k != 0 and freq[i] != []:
                result.append(freq[i])
                k -= 1
        return result

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = [1] * len(nums)
    #     # calculate the prefix, prefix means previous values's multiple
    #     prefix = 1
    #     for i in range(len(nums)):
    #         res[i] = prefix
    #         prefix *= nums[i]
    #     postfix = 1
    #     # calculate the postfix, postfix means values behind the values' multiple
    #     for i in range(len(nums)-1, -1, -1):
    #         res[i] *= postfix
    #         postfix *= nums[i]
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = res[i]*prefix
            prefix = nums[i]*prefix
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*prefix
            prefix = prefix*nums[i]
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
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
        longest = 0
        number = set(nums)
        for num in nums:
            length = 1
            current_number = num+1
            while True:
                if current_number in number:
                    length+=1
                    longest = max(longest,length)
                    current_number+=1
                    continue
                break
        return longest



if __name__ == "__main__":
    arrayHash = ArrayHash()
    # arrayHash.longestConsecutive([100, 4, 200, 1, 3, 2])
    # print(arrayHash.decode(arrayHash.encode(["lint", "code", "love", "you"])))
    # print(arrayHash.containsDuplicate([1, 2, 3, 1]))
    # print(arrayHash.isAnagram("anagram", "nagaram"))
    # print(arrayHash.twoSum([2, 7, 11, 15], 9))
    # print(arrayHash.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(arrayHash.topKFrequent([7, 7, 7, 7, 7, 2, 1, 2, 3], 2))
    # print(arrayHash.productExceptSelf([1, 2, 3, 4]))
    arrayHash.longestConsecutive([100,4,200,1,3,2])
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
