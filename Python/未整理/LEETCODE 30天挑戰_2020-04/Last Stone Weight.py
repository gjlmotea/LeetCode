from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1 = max(stones)
            stones.remove(max1)
            
            max2 = max(stones)
            stones.remove(max2)
            
            last = max1 - max2
            if last != 0:
                stones.append(max1-max2)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
        

print(Solution().lastStoneWeight([2,2]))
print(Solution().lastStoneWeight([2,7,4,1,8,1]))


##class Solution:
##    def lastStoneWeight(self, stones: List[int]) -> int:
##        for i in range(len(stones) - 1):
##            stones.sort()
##            stones.append(stones.pop() - stones.pop()) 
##        return stones[0]
##		


##import heapq
##class Solution:
##    def lastStoneWeight(self, stones: List[int]) -> int:
##        stones = [-val for val in stones]
##        heapq.heapify(stones)
##        while len(stones) > 1:
##            x1 = heapq.heappop(stones)
##            x2 = heapq.heappop(stones)
##            if x1 != x2:
##                heapq.heappush(stones,-abs(x1-x2))
##        if len(stones) == 0:
##            return 0
##        return -stones[0]


##
##class Solution:
##    def lastStoneWeight(self, stones: List[int]) -> int:
##        while len(stones) > 1:
##            stones = sorted(stones)
##            replacement = stones[-1] - stones[-2]
##            if replacement != 0:
##                stones = stones[:-2] + [replacement]
##            else:
##                stones = stones[:-2]
##        return stones[0] if stones else 0
