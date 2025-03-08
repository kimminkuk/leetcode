class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b_field = []
        st,ed = -1, -1
        _min = len(blocks)
        #temp = 0
        for i in range(len(blocks)-k+1):
            temp = 0
            for j in range(i, k+i):
                if blocks[j] == "W":
                    temp+=1
            if _min > temp:
                _min = temp
        return _min