class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mDict = {}
        for m in magazine:
            if m in mDict:
                mDict[m] += 1
            else:
                mDict[m] = 1
        
        for r in ransomNote:
            if r in mDict:
                mDict[r] -= 1
                if mDict[r] < 0:
                    return False
            else:
                return False
        return True
        
print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("abc", "bacb"))
print(Solution().canConstruct("ccczccczx", "cccccc"))
print(Solution().canConstruct("eggmax", "eggmic"))

##class Solution:
##    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
##        for item in ransomNote:
##            if not item in magazine:
##                return False
##            magazine = magazine.replace(item, "", 1)
##        return True
