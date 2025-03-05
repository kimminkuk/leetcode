class Solution:
    def coloredCells(self, n: int) -> int:
        if n <= 1:
            return 1
        
        ans = 1
        mid = n * 2 - 1        
        for i in range(2, n):
            ans += (i - 1) * 2 + 1
        
        
        return ans * 2 + mid        