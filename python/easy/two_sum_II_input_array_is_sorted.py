# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Attempted Solution
# def twosum(numbers, target):
#   result = []
#   for i in numbers:
#     for j in numbers[numbers.index(i)+1:]:
#       if i + j == target:
#         result.append(numbers.index(i) + 1)
#         result.append(numbers.index(j) + 1)
#         print(result)

# Best Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers) - 1
            
        while a < b:
            c = numbers[a] + numbers[b]
            if c == target:
                return [a+1, b+1]
            elif c < target:
                a += 1
            else:
                b -= 1


numbers = [2,7,11,15]
target = 9
two_sum(numbers, target)