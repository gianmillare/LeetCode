// 1768. Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

var mergeAlternately = function(word1, word2) {
    var maxLength = Math.max(word1.length, word2.length);
    var answer = [];
    
    for (var i = 0; i < maxLength; i++) {
        if (i < word1.length) {
            answer.push(word1[i]);
        }
        
        if (i < word2.length) {
            answer.push(word2[i]);
        }
    }
    
    return answer.join("");
};