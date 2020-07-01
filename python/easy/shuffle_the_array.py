# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        i = 0
        while i < n:
            x.append(nums.pop(0))
            i += 1
        
        y = nums
        
        results = []
        for i in range(0, len(y)):
            results.append(x[i])
            results.append(y[i])
        
        return results