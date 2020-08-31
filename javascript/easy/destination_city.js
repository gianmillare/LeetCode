// 1436. Destination City
// https://leetcode.com/problems/destination-city/

var destCity = function(paths) {
    var ans = [];
    
    for (var i = 0; i < paths.length; i++) {
        ans.push(paths[i][0]);
    }
    
    for (var i = 0; i < paths.length; i++) {
        if ( !(ans.includes(paths[i][1])) ) {
            return paths[i][1];
        }
    }
};

console.log(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))