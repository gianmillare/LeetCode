# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
  if s is None:
    return True

  lst = list(s)
  new_list = []

  for i in lst:
    if i.isalnum():
      new_list.append(i.lower())
  
  if new_list == new_list[::-1]:
    print("True")
  else:
    print("False")


    


s = "A man, a plan, a canal: Panama"
isPalindrome(s)