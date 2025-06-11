class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for _ in range(rowIndex):
            dummy = [0] + res[-1] + [0]
            cur_arr = []
            for i in range(len(res) + 1):
                cur_arr.append(dummy[i] + dummy[i+1])
            res.append(cur_arr)
        return res[rowIndex]