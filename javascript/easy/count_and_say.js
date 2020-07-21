// 38. Count and Say
// https://leetcode.com/problems/count-and-say/

const countAndSay = function(n) {
    var str = '1';
    while (n > 1) {
        var newStr = '', count = 0, say = str[0];
        for (var i = 0; i <str.length; i++) {
            if (str[i] === say) {
                count++;
            } else {
                newStr += count + say;
                count = 1;
                say = str[i];
            }
        }
        str = newStr + count + say;
        n--;
    }
    return str;
};