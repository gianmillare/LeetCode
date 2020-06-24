# 169. Majority Element
# https://leetcode.com/problems/majority-element/

def majorityelement(nums):
  results = [1]
  nums_set = set(nums)
  count = 0
  for i in nums_set:
    x = nums.count(i)
    if x > count:
      count = x
      results.pop(0)
      results.append(i)
  
  print(results[0])

# Best Solution
# return sorted(num)[len(num)/2]

nums = [3,2,3]
majorityelement(nums)