def length_of_last_word(s):
  lis = s.split()
  if len(lis) > 0:
    return len(lis[-1])
  else:
    return 0

n = " "
length_of_last_word(n)