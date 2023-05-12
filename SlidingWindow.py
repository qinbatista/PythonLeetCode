
import collections
import math
from typing import List


class SlidingWindow:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = max(profit, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right-left+1)
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r-l+1)-maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1
        return matches == 26


if __name__ == "__main__":
    tp = SlidingWindow()
    # print(tp.maxProfit([7,1,5,3,6,4]))
    print(tp.lengthOfLongestSubstring("pwwkew"))
