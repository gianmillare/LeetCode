// 1342. Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

var numberOfSteps  = function(num) {
    if (num == 0) {
        return 0;
    }
    
    if (num == 1) {
        return 1;
    }
    
    var count = 0;
    while (num != 0) {
        if (num % 2 == 0) {
            num = num / 2;
            count++;
        }
        if (num % 2 != 0) {
            num--;
            count++;
        }
    }
    return count;
};