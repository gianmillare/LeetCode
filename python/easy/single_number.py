# # 136. Single Number
# # https://leetcode.com/problems/single-number/

def single_number(nums):
  for i in nums:
    if nums.count(i) == 1:
      print(i)
    else:
      pass

# Faster Solution
def singleNumbers(nums):
  print(2 * sum(set(nums)) - sum(nums))
  # by multiplying the set by 2 and subtracting the sum of the original
  # the resulting integer is a "copy" of the single digit integer



nums = [4,1,2,1,2]
singleNumbers(nums)

