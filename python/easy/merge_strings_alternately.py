# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = max([len(word1), len(word2)])
        answer = []
        for i in range(0, max_length):
            if i < len(word1):
                answer.append(word1[i])
            if i < len(word2):
                answer.append(word2[i])
        return "".join(answer)