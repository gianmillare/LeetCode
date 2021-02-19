# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

def interpret(command):

    parsed_command = []

    for i in range(len(command)):
        if command[i] == "G":
            parsed_command.append("G")
        elif command[i] == "(" and command[i + 1] == ")":
            parsed_command.append("o")
        elif command[i] == "(" and command[i + 1] == "a":
            parsed_command.append("al")

    return "".join(parsed_command)

print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))