class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        seen = [[float('inf')] * m for _ in range(n)]
        
        hq = []
        heapq.heappush(hq, (0,0,0))
        moveTime[0][0]=0
        while hq:
            cur_time, cur_row, cur_col = heapq.heappop(hq)
            if cur_time >= seen[cur_row][cur_col]:
                continue
            seen[cur_row][cur_col] = cur_time
            if cur_row == n-1 and cur_col == m-1:
                return cur_time
            for row, col in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_row, next_col = cur_row+row, cur_col+col
                if 0 <= next_row < n and 0 <= next_col < m and seen[next_row][next_col] == float('inf'):
                    t = moveTime[next_row][next_col]
                    max_t = max(t, cur_time)+1
                    heapq.heappush(hq, (max_t, next_row, next_col))
        return 0