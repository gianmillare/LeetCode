# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/

# My Solution (works when executed independently from Leetcode)
def trailing_zeroes(n):
  fact_result = fact(n)
  listed_result = [int(i) for i in str(fact_result)]
  return listed_result.count(0)

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)

n = 3
print(trailing_zeroes(n))

# Solution accepted by Leetcode / Best Solution
# Note that in order to get a '0' at the end, the input must include a multiple of 5 --> getting a factorial of a multiple of 5
# So, depending on n / 5, the zeroes will increment by 1

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n != 0:
            n = n // 5
            result += n
        return result
        

