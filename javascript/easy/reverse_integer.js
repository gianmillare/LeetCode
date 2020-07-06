// 7. Reverse Integer
// https://leetcode.com/problems/reverse-integer/

var reverse = function(x) {
    var x = x.toString();
    var list_x = x.split('');
    var reversed_list = list_x.reverse();

    var last_element = reversed_list[reversed_list.length - 1];

    if (last_element == "-") {
        reversed_list.pop();
        reversed_list.unshift("-");
    }

    var result = reversed_list.join('');
    var final = parseInt(result);

    const upper_bounds = Math.pow(2, 31) - 1;
    const lower_bounds = Math.pow(2, 31) * -1;

    if (final < lower_bounds || final > upper_bounds) {
        return 0;
    } else {
        return final;
    }
}