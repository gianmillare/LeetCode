# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = []
        for i in A:
            ans.append(i**2)
        
        return sorted(ans)
            
# Best Solution
# return sorted(x*x for x in A)