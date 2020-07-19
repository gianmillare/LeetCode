// 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

var searchInsert = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target);
    } else if (target > nums[nums.length - 1]) {
        return nums.length;
    } else {
        for (var i = 0; i < nums.length; i++) {
            if (nums[i] > target) {
                return i;
            }
        }
    }
};

// console.log(searchInsert([1,3,5,6], 5))
console.log(searchInsert([1,3,5,6], 2))