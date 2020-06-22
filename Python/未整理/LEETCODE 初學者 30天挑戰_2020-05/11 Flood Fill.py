from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        Color = image[sr][sc]
        if Color == newColor:
            return image
        
        self.DFS(image, sr, sc, Color, newColor)
        return image
    def DFS(self, image, r, c, Color, newColor):
        image[r][c] = newColor
        if r+1 < len(image) and image[r+1][c] == Color:
            self.DFS(image, r+1, c, Color, newColor)
        if r-1 >= 0 and image[r-1][c] == Color:
            self.DFS(image, r-1, c, Color, newColor)
        if c+1 < len(image[0]) and image[r][c+1] == Color:
            self.DFS(image, r, c+1, Color, newColor)
        if c-1 >= 0 and image[r][c-1] == Color:
            self.DFS(image, r, c-1, Color, newColor)

print(Solution().floodFill([[1,5,1],[1,1,0],[1,9,1]],1,1,2))
print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        color = image[sr][sc]
        if newColor == color:
            return image

        self.dfs(image, sr, sc, newColor, color)
        return image

    def dfs(self, image, r, c, newColor, color):
        m, n = len(image), len(image[0])
        directions = [(0,-1), (1,0), (0,1), (-1,0)]
        image[r][c] = newColor
        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == color:
                self.dfs(image, nr, nc, newColor, color)




from collections import deque
def isSafeIndex(image, r, c):
    if r<0 or c<0 or r>=len(image) or c>=len(image[0]):
        return False
    return True

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # nothing to change
        if image[sr][sc] == newColor: return image

        # iterative way of dfs
        que = deque([])
        que.append([sr, sc])
        oldColor = image[sr][sc]
        while que:
         curr_r, curr_c = que.popleft()
         image[curr_r][curr_c] = newColor
         for r, c in [[1,0], [0,1], [-1,0], [0,-1]]:
             new_r, new_c = curr_r + r, curr_c + c
             if isSafeIndex(image, new_r, new_c) and image[new_r][new_c] == oldColor:
                 que.append([new_r, new_c])
        return image
