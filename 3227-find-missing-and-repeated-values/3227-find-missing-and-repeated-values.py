class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # dict gogo
        grid_sum = (len(grid) * len(grid[0])) * ((1+(len(grid) * len(grid[0]))) / 2)
        d = {}
        ans = [0, 0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] not in d:
                    d[grid[row][col]] = 1
                    grid_sum -= grid[row][col]
                else:
                    # d[grid[row][col]] += 1
                    ans[0] = grid[row][col]
        ans[1] = int(grid_sum)
        return ans