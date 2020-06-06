def bruteForcetwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                print([i, j])

# Solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            total = nums[i] + nums[j]
            if total == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9
bruteForcetwoSum(nums, target)

