dict = {
    1: 1,
    2: 2
}


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            
            for i in range(3, n+1):
                x = dict[i-1] + dict[i-2]
                dict[i] = x
                
            return dict[n]


n = 5
climbStairs(n)