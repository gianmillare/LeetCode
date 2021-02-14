// 771. Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

var numJewelsInStones = function(jewels, stones) {
    var count = 0;
    
    for (var i = 0; i < stones.length; i++) {
        if ( jewels.includes(stones[i]) ) {
            count ++;
        }
    }
    
    return count;
};