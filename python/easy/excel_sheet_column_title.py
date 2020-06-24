# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/

def convert_to_title(n):
  # Create an empty list to store all values of alphabet 65-90
  alpha_list = []
  for i in range(ord('A'), ord('Z')+1):
    alpha_list.append(chr(i))
  
  # create an empty list to store alpha-char
  results = []
  while n > 0:
    # Subtract 1 from n because list comprehension starts at 0
    # obtain the modulus of 26 from n and append it to results for the first letter
    results.append(alpha_list[(n-1)%26])
    # obtain the floored value of n-1 and loop again until n = 0
    n = (n-1) // 26
  
  # reverse the results list
  results.reverse()
  return ''.join(results)



n = 28
convert_to_title(n)