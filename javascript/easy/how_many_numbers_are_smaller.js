// 1365. How Many Numbers Are Smaller Than the Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

var smallerNumbersThanCurrent = function(nums) {
    var answer = [];
    for (var i = 0; i < nums.length; i++) {
        var count = 0;
        for (var j = 0; j < nums.length; j++) {
            if (nums[i] > nums[j]) {
                count++;
            }
        }
        answer.push(count);
    }
    return answer;
};