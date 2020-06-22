class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for s in S:
            if s in J:
                ans += 1
        return ans
    

print(Solution().numJewelsInStones("aA","aAAbbbb"))

##class Solution:
##    def numJewelsInStones(self, J: str, S: str) -> int:
##        jewels = set(J)
##        count = 0
##        for stone in S:
##            count += 1 if stone in jewels else 0
##        return count


##class Solution:
##    def numJewelsInStones(self, J: str, S: str) -> int:
##        res, count = 0, {}
##        
##        for l in S:
##            if l in count: count[l] += 1
##            else: count[l] = 1
##        
##        for l in J:
##            if l in count:
##                res += count[l]
##        
##        return res
