class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return (strs[0])

        prefix = strs[0]
        p_length = len(prefix)

        for i in strs[1:]:
            while prefix != i[0:p_length]:
                prefix = prefix[0:p_length - 1]
                p_length = len(prefix)

                if p_length == 0:
                    return ("")

        return (prefix)