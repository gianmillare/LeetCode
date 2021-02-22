# 1342. Number of Steps to Reduce a Number to Zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num == 1:
            return 1
        
        count = 0
        
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                count = count + 1
            if num % 2 != 0:
                num = num - 1
                count = count + 1
        
        return count