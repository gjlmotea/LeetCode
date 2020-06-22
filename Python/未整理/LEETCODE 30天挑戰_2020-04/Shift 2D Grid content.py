from typing import List
import copy

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        board = copy.deepcopy(grid)
        k = len(grid) * len(grid[0]) - k
        while k < 0:
            k = k + len(grid) * len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                x = i
                y = j + k
                while y >= len(grid[0]):
                    x = x + 1
                    y = y - len(grid[0])
                while x >= len(grid):
                    x = x - len(grid)
                    
                #print("===xy:", x, y)
                #print(grid)
                board[i][j] = grid[x][y]
                
                
                #print(grid[i][j], end = '')
            #print()
        #print(board)
        #print(grid)
        return board

#print(Solution.shiftGrid(object(), [[1,2,3],[4,5,6],[7,8,9]], k = 100))

print(Solution.shiftGrid(object(), [[1],[2],[3],[4],[5],[6],[7]], k = 10))
