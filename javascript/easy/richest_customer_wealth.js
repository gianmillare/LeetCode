// 1672. Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

var maximumWealth = function(accounts) {
    var wealthArray = [];
    for (var i = 0; i < accounts.length; i++) {
        wealthArray.push(accounts[i].reduce((a, b) => a + b, 0))
    }
    
    return wealthArray.reduce(function(a, b) {
        return Math.max(a, b);
    })
};

console.log(maximumWealth([[1,2,3],[3,2,1]]));