// 1281. Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

var subtractProductAndSum = function(n) {
    var digits = n.toString().split("");
    var product = 1;
    var summed = 0;

    for (var i = 0; i < digits.length; i++) {
        product = product * parseInt(digits[i]);
        summed = summed + parseInt(digits[i]);
    }

    return product - summed;
};

console.log(subtractProductAndSum(234));