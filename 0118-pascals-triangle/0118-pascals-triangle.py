class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #left, right
        # left, right   left, right
        dq = deque()
        result = []
        for num in range(1, numRows + 1):
            cur_level = []
            if num <= 2:
                cur_level = [1] * num
            else:
                cur_level = [1] + [0] * (num-2) + [1]
                for mid in range(num-2):
                    cur_level[1 + mid] = result[-1][mid]+result[-1][mid+1]
            result.append(cur_level)
        return result
