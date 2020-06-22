class Solution:
    def firstUniqChar(self, s: str) -> int:
        cDict = {}
        ans = -1
        for c in s:
            if c in cDict:
                cDict[c] += 1
            else:
                cDict[c] = 1
        for i, c in enumerate(s):
            if cDict[c] == 1:
                return i
        return ans

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar(""))
print(Solution().firstUniqChar("cc"))
