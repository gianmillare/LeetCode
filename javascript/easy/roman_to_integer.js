// 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

var romanToInt = function(s) {
    var romanNumerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    var ans = 0;
    
    list_s = s.split('');

    if (list_s.length == 1) {
        ans += romanNumerals[s[0]];
    } else {
        for (var i = 0; i < list_s.length - 1; i++) {
            if (romanNumerals[list_s[i]] >= romanNumerals[list_s[i + 1]]) {
                ans += romanNumerals[list_s[i]];
            } else {
                ans -= romanNumerals[list_s[i]];
            }
        }
        ans += romanNumerals[list_s[list_s.length - 1]];
    }

    return ans;
    
};