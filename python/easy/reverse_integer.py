def reverse(x):
    x = str(x)
    lis_x = []
    reversed_lis = []

    for i in x:
        lis_x.append(i)

    for i in reversed(x):
        reversed_lis.append(i)

    if reversed_lis[-1] == "-":
        reversed_lis.pop()
        reversed_lis.insert(0, "-")
    else:
        pass

    reversed_final = ''.join(str(i) for i in reversed_lis)
    reversed_final = int(reversed_final)

    if -2**31 <= reversed_final <= 2**31 - 1:
        print(reversed_final)
    else:
        print(0)

n = 123
reverse(n)

# n = -2**31
# print(n)
# n = 2**31 - 1
# print(n)