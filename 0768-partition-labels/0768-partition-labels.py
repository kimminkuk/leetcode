class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d_move = Counter(s)
        d_ori = Counter(s)
        
        _len = 0
        ans = []
        chk = 0
        for el in s:
            _len += 1
            if d_ori[el] == d_move[el]:
                chk += 1
            
            d_move[el] -= 1
            if d_move[el] == 0:
                chk -= 1
            
            if chk == 0:
                ans.append(_len)
                _len = 0
        
        return ans
        