// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

var longestCommonPrefix = function(strs) {
//     get rid of the base case
    if (strs.length === 0 || strs === undefined){return "";}
    if (strs.length === 1){return strs[0];}
    
//     get the first string in the array and use it as the base --> flower
    var prefix = strs[0];
//     get the length of the str and store it in a variable
    var p_length = prefix.length; // --> 6
    
//     Loop through the rest of the array
    for (var i = 1; i < strs.length; i++) {
//         while the prefix does not equal the rest of the list, drop the last letter
        while (!(prefix == strs[i].substring(0, p_length))) {
            prefix = prefix.substring(0, prefix.length -1 );
            p_length = prefix.length;
            
//             if the length hits 0, return ""
            if (p_length === 0) {
                return "";
            }
        }
    }
    return prefix;
};

console.log(longestCommonPrefix(["c","acc","ccc"]));