class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # 예측이 아니라..
        # In-Memory 전략이였네 아..
        eras = self.get_eratosthenes(right)
        eras_sort = [i for i in range(left, right+1) if eras[i]]
        
        _min = [-1, -1]
        _min_diff = pow(10,6)
        for i in range(len(eras_sort)-1):
            temp = eras_sort[i+1] - eras_sort[i]
            if temp < _min_diff:
                _min_diff = temp
                _min = [eras_sort[i], eras_sort[i+1]]
        return _min
    
    def get_eratosthenes(self, n):
        eras = [True] * (n+1)
        if n < 2:
            for i in range(n):
                eras[i] = False
        else:
            eras[0]=eras[1]=False
            for i in range(2, int(math.sqrt(n))+1):
                if eras[i]:
                    for j in range(i*2, n+1, i):
                        eras[j] = False
        return eras
