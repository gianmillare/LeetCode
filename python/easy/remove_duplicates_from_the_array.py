def removeDuplicates(nums):
  index = 0

  for index in range(0, len(nums)):
    if nums[index] in nums[index+1:]:
      nums.remove(nums[index])
    else:
      index += 1

nums = [1,1,2]
removeDuplicates(nums)