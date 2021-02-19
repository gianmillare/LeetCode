// 1678. Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

var interpret = function(command) {
    var parsed_command = [];
    
    for (var i = 0; i < command.length; i++) {
        if (command[i] == "G") {
            parsed_command.push("G");
        } else if ( (command[i] == "(") && (command[i + 1] == ")") ) {
            parsed_command.push("o");
        } else if ( (command[i] == "(") && (command[i + 1] == "a") ) {
            parsed_command.push("al");
        }
    }
    
    return parsed_command.join("");
};