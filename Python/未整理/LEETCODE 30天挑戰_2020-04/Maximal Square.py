from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        y_len = len(matrix)
        if y_len == 0:
            x_len = 0
        else:
            x_len = len(matrix[0])
        maxLen = 0
        for y in range(y_len):
            for x in range(x_len):
                if matrix[y][x] == '1':
                    SqLen = 1
                    SqJudge = True
                    while x+SqLen < x_len and y+SqLen < y_len and SqJudge:
                        isAll1 = True
                        for b in range(0, SqLen+1):
                            for a in range(0, SqLen+1):
                                if matrix[y+b][x+a] != '1':
                                    isAll1 = False
                                    break
                                if isAll1 == False:
                                    print("BBBBBBBBBBBBBB", isAll1)
                        if isAll1:
                            SqLen += 1
                        else:
                            SqJudge = False
                    #print(y, x, ":", SqLen)
                    maxLen = max(maxLen, SqLen)
                #print(matrix[y][x], end = '')
            #print()
        
        return maxLen * maxLen

print(Solution().maximalSquare([]))
print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(Solution().maximalSquare([
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","0","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"]
]))

print(Solution().maximalSquare([
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"],
["1","1","1","1","1","1"]
]))


##暴力法
##class Solution:
##    def maximalSquare(self, matrix: List[List[str]]) -> int:
##        y_len = len(matrix)
##        if y_len == 0:
##            x_len = 0
##        else:
##            x_len = len(matrix[0])
##        maxLen = 0
##        for y in range(y_len):
##            for x in range(x_len):
##                if matrix[y][x] == '1':
##                    SqLen = 1
##                    SqJudge = True
##                    while x+SqLen < x_len and y+SqLen < y_len and SqJudge:
##                        isAll1 = True
##                        for b in range(0, SqLen+1):
##                            for a in range(0, SqLen+1):
##                                if matrix[y+b][x+a] != '1':
##                                    isAll1 = False
##                        if isAll1:
##                            SqLen += 1
##                        else:
##                            SqJudge = False
##                    #print(y, x, ":", SqLen)
##                    maxLen = max(maxLen, SqLen)
##                #print(matrix[y][x], end = '')
##            #print()
##        
##        return maxLen * maxLen
