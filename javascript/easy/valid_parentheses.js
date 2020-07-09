// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/submissions/

var isValid = function(s) {
    var x = [];
    
    for (var i = 0; i < s.length; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            x.push(s[i]);
            }
        else {
            if (!(x.length == 0)) {
                if ( s[i] == ')' && (!(x[x.length - 1] == '(')) || s[i] == ']' && (!(x[x.length - 1] == '[')) || s[i] == '}' && (!(x[x.length - 1] == '{')) ) {
                    return false;
                }
                else {
                    x.pop();
                }
            }
            else {
                return false;
            }
        }
    }
    if (x.length == 0) {
        return true;
    }
    else {
        return false;
    }
};