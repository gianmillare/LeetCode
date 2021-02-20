// 1389. Create Target Array in the Given Order
// https://leetcode.com/problems/create-target-array-in-the-given-order/

var createTargetArray = function(nums, index) {
    var answer = []
    
    for (var i = 0; i < nums.length; i++) {
        answer.splice(index[i], 0, nums[i]);
    }
    
    return answer;
};