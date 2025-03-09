class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dq = deque()
        w_color = 0
        for i in range(k):
            dq.append(blocks[i])
            if blocks[i] == "W":
                w_color += 1
        
        st = 0
        _min = w_color
        for i in range(k, len(blocks)):
            
            if dq[st] == "W":
                w_color -= 1
            dq.popleft()
            
            if blocks[i] == "W":
                w_color += 1
            dq.append(blocks[i])
            if _min > w_color:
                _min = w_color
        return _min