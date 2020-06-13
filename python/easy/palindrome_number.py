class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        lis = []
        reversed_lis = []

        for i in x:
            lis.append(i)

        for i in reversed(x):
            reversed_lis.append(i)

        final_lis = ''.join(str(i) for i in lis)
        final_reversed_lis = ''.join(str(i) for i in reversed_lis)

        if final_lis == final_reversed_lis:
            return True
        else:
            return False