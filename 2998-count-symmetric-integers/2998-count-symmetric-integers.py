class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def div(num):
            _ten = 0
            ori_num = num
            while num > 0:  # _ten -> 9 -> 90 -> 900 ... 10^n * 9
                num = int(num // 10)
                if _ten == 0 : _ten = 1
                else: _ten *= 10
                
            arr = []
            while _ten > 0:
                step_1 = int(ori_num // _ten)
                arr.append(step_1)
                ori_num = ori_num - step_1 * _ten 
                _ten = int(_ten//10)
            
            return arr

        ans = 0
        for i in range(low, high+1):
            arr = div(i)
            arr_len = len(arr)
            if arr_len % 2 == 0:
                left = arr_len // 2
                if sum( arr[ : left] ) == sum( arr[left : ] ):
                    ans += 1
        return ans
