// 1528. Shuffle String
// https://leetcode.com/problems/shuffle-string/

var restoreString = function(s, indices) {
    var ans = [];
    for (var i = 0; i < s.length; i++) {
        ans.push(s[indices.indexOf(i)])
    }
    
    return ans.join("");
};