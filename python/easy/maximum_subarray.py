def maxSubArray(nums):
    # get the max of nums[i] and nums[i-1] and store them in a variable max_sum
    # as values are stored in max_sum, get the max(max_sum) continually updated in real_max

    total_sum = max_sum = nums[0]

    for i in nums[1:]:
        total_sum = max(i, total_sum+i)
        max_sum = max(max_sum, total_sum)

    print(max_sum)



n = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(n)