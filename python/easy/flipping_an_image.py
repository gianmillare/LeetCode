# 110     011     100
# 101     101     010
# 000     000     111

# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[(1 - j)for j in i[::-1]] for i in A]
