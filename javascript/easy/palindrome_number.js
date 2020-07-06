// 9. Palindrome Number
// https://leetcode.com/problems/palindrome-number/

var isPalindrome = function(x) {
    if (x < 0) {
        return false;
    }

    list_x = x.toString().split('');
    reversed_x = list_x.reverse().join('');
    
    if (x == parseInt(reversed_x)) {
        return true;
    } else {
        return false;
    }
};

console.log(isPalindrome(121));