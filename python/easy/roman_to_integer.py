class Solution:
    def romanToInt(self, s: str) -> int:
        results = 0

        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            results = dic[s[0]]
        else:
            for i in range(0, len(s) - 1):
                if dic[s[i]] >= dic[s[i + 1]]:
                    results += dic[s[i]]
                else:
                    results -= dic[s[i]]

            results += dic[s[-1]]

        return results