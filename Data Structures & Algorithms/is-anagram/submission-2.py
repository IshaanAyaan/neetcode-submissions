class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}

        if len(s) != len(t):
            return False

        for y in range(len(s)):
            if s[y] in check:
                check[s[y]] +=1
            if s[y] not in check:
                check[s[y]] = 1

        for i in range(len(t)):
            if t[i] not in check or check[t[i]] == 0:
                return False
            if t[i] in check:
                check[t[i]] -= 1
        return True