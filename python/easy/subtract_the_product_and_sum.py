# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

def subtractProductAndSum(n):
    # split the integer into digits
    digits = [int(i) for i in list(str(n)) ]

    # find the product/sum of all digits
    product, summed = 1, 0
    for i in digits:
        product = product * i 
        summed = summed + i
    
    return product - summed

print(subtractProductAndSum(234))