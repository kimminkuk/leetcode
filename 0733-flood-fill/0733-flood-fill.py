class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = []
        ans_image = image
        ori_color = image[sr][sc]
        def fill_image(image, row, col, color, visited):
            if (row, col) not in visited:
                if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == ori_color: 
                    visited.append((row, col))                    
                    image[row][col] = color
                    fill_image(image, row+1, col, color, visited)
                    fill_image(image, row-1, col, color, visited)
                    fill_image(image, row, col+1, color, visited)
                    fill_image(image, row, col-1, color, visited)
                
        
        fill_image(ans_image, sr, sc, color, visited)    
        return ans_image    