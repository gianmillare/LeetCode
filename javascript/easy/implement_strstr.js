// 28. Implement strStr()
// https://leetcode.com/problems/implement-strstr/

var strStr = function(haystack, needle) {
    if (needle.length == 0) {
        return 0;
    } else if (haystack.includes(needle)) {
        for (var i = 0; i <= haystack.length; i++) {
            if (haystack.substring(i, i + needle.length) == needle) {
                return i;
            }
        }
    } else {
        return -1;
    }
};

var h = "hello";
var n = "ll";
console.log(strStr(h, n));