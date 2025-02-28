class Solution:
    def scoreOfString(self, s: str) -> int:
        s_list = list(s)
        s_len = len(s_list)
        ans = 0
        for i in range(s_len-1):
            ans += abs(ord(s_list[i]) - ord(s_list[i+1]))
        
        return ans
            