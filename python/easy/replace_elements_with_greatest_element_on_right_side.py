# 1299. Replace Elements with Greatest Element on Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        results = [-1]
        greatest_num = 0

        for i in arr[::-1]:
            if i > greatest_num:
                greatest_num = i
            results.append(greatest_num)

        results.pop()
        return results[::-1]
