class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        last_end = 0
        ans = 0
        for start,end in meetings:
            if start > last_end + 1:
                ans += start - (last_end + 1)
            last_end = max(last_end, end)
        
        return ans + (days-last_end)