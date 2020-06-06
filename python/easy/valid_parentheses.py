def isValid(s):
    x = []

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            x.append(s[i])
        else:
            if len(x) != 0:
                if (s[i] == ')' and x[-1] != '(') or (s[i] == ']' and x[-1] != '[') or (s[i] == '}' and x[-1] != '{'):
                    return False
                else:
                    x.pop()
            else:
                return False

    if len(x) == 0:
        return True
    else:
        return False



s = "{[]}"
isValid(s)


