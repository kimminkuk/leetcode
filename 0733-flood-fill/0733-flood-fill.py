class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #sr -> col, y   sc -> row, x
        maxX = len(image[0])
        maxY = len(image)
        target = image[sr][sc]
        if target == newColor:
            return image
        
        def dfs(x, y):
            if 0 <= x < maxX and 0 <= y < maxY and target == image[y][x]:
                image[y][x] = newColor
                dfs(x-1, y) #left
                dfs(x+1, y) #right
                dfs(x, y-1) #up
                dfs(x, y+1) #down
                
        dfs(sc, sr)
        return image