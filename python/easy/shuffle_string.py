# 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/

def restoreString(s, indices):
        answer = []
        for i in range(len(indices)):
            answer.append(s[indices.index(i)])
        
        return "".join(answer)

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))