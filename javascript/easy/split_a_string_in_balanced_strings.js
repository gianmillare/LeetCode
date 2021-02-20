// 1221. Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

var balancedStringSplit = function(s) {
    var counts = {
        "r_count": 0,
        "l_count": 0,
        "substring": 0
    };
    
    for (var i = 0; i < s.length; i++) {
        if ( s[i] == "R" ) {
            counts["r_count"]++;
        } else if ( s[i] == "L" ) {
            counts["l_count"]++;
        }
        
        if ( (counts["r_count"] > 0) && (counts["l_count"] > 0) && (counts["r_count"] == counts["l_count"]) ) {
            counts["substring"]++;
        }
    }
    
    return counts["substring"];
};