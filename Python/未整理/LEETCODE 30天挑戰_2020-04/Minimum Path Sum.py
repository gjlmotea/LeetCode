from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        y_len = len(grid)
        if len(grid) == 0:
            x_len = 0
        else:
            x_len = len(grid[0])
        def show():
            for y in range(y_len):
                for x in range(x_len):
                    print(grid[y][x], end = '')
                print()
            print()
            
        show()
            
        for y in range(y_len - 1):
            grid[y+1][0] += grid[y][0]

        for x in range(x_len - 1):
            grid[0][x+1] += grid[0][x]

        for y in range(1, y_len):
            for x in range(1, x_len):
                grid[y][x] = grid[y][x] + min(grid[y-1][x], grid[y][x-1])
        
        show()
        
        return grid[y_len-1][x_len-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

##class Solution(object):
##    def minPathSum(self, grid):
##        y_len = len(grid)
##        if len(grid) == 0:
##            x_len = 0
##        else:
##            x_len = len(grid[0])
##        def show():
##            for y in range(y_len):
##                for x in range(x_len):
##                    print(grid[y][x], end = '')
##                print()
##            print()
##        show()
##
##        
##        dp = [0]*len(grid)
##        dp[0] = grid[0][0]
##        for i in range(1,len(grid)) :
##            dp[i] = dp[i-1] + grid[i][0]
##        print(dp)
##        for j in range(1, len(grid[0])) :
##            for i in range(len(grid)) :
##                dp[i] = min(dp[i], dp[i-1]) + grid[i][j] if i > 0 else dp[i]+grid[i][j]
##                print(dp)
##        
##        return dp[len(grid)-1]




class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if r==0 and c==0: # We just want to skip the top-left corner of the grid
                    continue
                if r-1<0: # Cases for elements in top row
                    grid[r][c] = grid[r][c] + grid[r][c-1]  
                elif c-1<0: # Cases for elements in leftmost column
                    grid[r][c] = grid[r][c] + grid[r-1][c]  
                else: # Normal cell
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])               
        
        return grid[rows-1][cols-1] # We have got the minimum path accumaled at the bottom-right corner, just return this
## https://leetcode.com/problems/minimum-path-sum/discuss/584967/Python-Grid-reduction-(Sounds-fancy-but-a-simple-method)-no-additional-space
