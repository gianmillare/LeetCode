# 198. House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        previous, current = 0, 0

        for i in nums:
            previous, current = current, max(previous + i, current)

        return current