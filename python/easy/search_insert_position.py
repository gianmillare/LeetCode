# Best solution
# def searchInsert(nums, target):
#     print(len([x for x in nums if x < target]))

def searchInsert(nums, target):
    lis = []
    for x in nums:
        if x < target:
            lis.append(x)
    print(len(lis))

n = [1,3,5,6]
m = 7

searchInsert(n, m)