class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        _min = len(blocks)
        w_l = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                w_l += 1
            if right - left + 1 == k:
                _min = min(_min, w_l)                
                if blocks[left] == "W":
                    w_l -= 1                
                left += 1
                    
        return _min