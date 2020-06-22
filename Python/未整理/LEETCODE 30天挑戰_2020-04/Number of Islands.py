from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(grid, y, x, y_len, x_len):
            if y<0 or x<0 or y>=y_len or x>=x_len:
                return
            if grid[y][x] == '0':
                return
            grid[y][x] = '0'
            DFS(grid, y+1, x, y_len, x_len)
            DFS(grid, y-1, x, y_len, x_len)
            DFS(grid, y, x+1, y_len, x_len)
            DFS(grid, y, x-1, y_len, x_len)

        y_len = len(grid)
        if y_len == 0:
            x_len = 0
        else:
            x_len = len(grid[0])
        ans = 0
        for y in range(y_len):
            for x in range(x_len):
                if grid[y][x] == '1':
                    DFS(grid, y, x, y_len, x_len)
                    ans += 1

        return ans

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(Solution().numIslands([]))


##class Solution:
##    def numIslands(self, grid: List[List[str]]) -> int:
##        def recurse(grid,r,c):
##            grid[r][c] = '0'
##            if r-1 >= 0 and grid[r-1][c] == '1':
##                recurse(grid,r-1,c)
##            if r+1 < len(grid) and grid[r+1][c] == '1':
##                recurse(grid,r+1,c)
##            if c-1 >= 0 and grid[r][c-1] == '1':
##                recurse(grid,r,c-1)
##            if c+1 < len(grid[0]) and grid[r][c+1] == '1':
##                recurse(grid,r,c+1)
##        
##        count = 0
##        for i in range(len(grid)):
##            for j in range(len(grid[0])):
##                if grid[i][j] == '1':
##                    count+=1
##                    recurse(grid,i,j)
##        return count



##import collections
##
##class Solution:
##    def numIslands(self, grid: List[List[str]]) -> int:
##        if grid is None or len(grid) < 1: return 0
##
##        num = 0
##        rows = len(grid)
##        cols = len(grid[0])
##
##        q = collections.deque()
##        for y in range(rows):
##            for x in range(cols):
##                if grid[y][x] == '1':
##                    num += 1
##                    q.append((y, x))
##                    while q:
##                        r, c = q.popleft()
##                        if r > 0 and grid[r - 1][c] == "1":
##                            grid[r - 1][c] = "0"
##                            q.append((r - 1, c))
##                        if r < rows - 1 and grid[r + 1][c] == "1":
##                            grid[r + 1][c] = "0"
##                            q.append((r + 1, c))
##                        if c > 0 and grid[r][c - 1] == "1":
##                            grid[r][c - 1] = "0"
##                            q.append((r, c - 1))
##                        if c < cols - 1 and grid[r][c + 1] == "1":
##                            grid[r][c + 1] = "0"
##                            q.append((r, c + 1))
##
##        return num
