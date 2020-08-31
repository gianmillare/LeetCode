# 1436. Destination City
# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ans = []
        
        for i in paths:
            ans.append(i[0])
        
        for i in paths:
            if i[1] not in ans:
                return i[1]