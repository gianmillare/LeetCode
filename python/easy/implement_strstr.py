def strtr(haystack, needle):
  if len(needle) == 0:
    print(0)
  elif needle in haystack:
    for i in range(0, len(haystack)):
      if haystack[i:i+len(needle)] == needle:
         print(i)
  else:
    print(-1)

h = "hello"
n = "o"
strtr(h, n)