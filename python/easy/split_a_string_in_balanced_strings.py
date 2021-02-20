# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count, l_count, substring = 0, 0, 0
        for i in s:
            if i == "R":
                r_count = r_count + 1
            elif i == "L":
                l_count = l_count + 1
            
            if r_count > 0 and l_count > 0 and r_count == l_count:
                substring = substring + 1
                r_count, l_count = 0, 0
        
        return substring