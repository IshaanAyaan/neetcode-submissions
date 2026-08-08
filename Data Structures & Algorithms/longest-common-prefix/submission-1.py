class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com = ""
        for char in range(len(min(strs))):
            temp = strs[0][char]
            for i in range(len(strs)):
                if strs[i][char] != temp:
                    return com
            com += temp
        return com
