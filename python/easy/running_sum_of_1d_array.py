# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)+1):
            res.append(sum(nums[:i]))
        return res

# Shorter but slower Solution
return accumulate(nums)