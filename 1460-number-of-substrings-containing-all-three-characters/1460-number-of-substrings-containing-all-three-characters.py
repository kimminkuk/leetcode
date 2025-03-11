class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        ans, right = 0, 0
        s_len = len(s)
        
        a,b,c = [], [], []
        for idx, el in enumerate(s):
            if el == "a":
                a.append(idx)
            elif el == "b":
                b.append(idx)
            elif el == "c":
                c.append(idx)
        
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        
        a_st, b_st, c_st = 0, 0, 0
        if a and b and c:
            a_st, b_st, c_st = a.pop(), b.pop(), c.pop()
            abc_min_idx = max(a_st, b_st, c_st)
            ans += (s_len - abc_min_idx)
        else:
            return ans
        
        while right < s_len:
            if s[right] == "a" and a:
                a_st = a.pop()
            elif s[right] == "b" and b:
                b_st = b.pop()
            elif s[right] == "c" and c:
                c_st = c.pop()
            else:
                return ans
            abc_min_idx = max(a_st, b_st, c_st)
            ans += (s_len - abc_min_idx)
            right+=1
            
        
        return ans
