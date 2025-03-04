class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # brute force?
        c = 0
        while pow(3, c) <= n:
            c += 1
        
        #1. bisect_left로 적절한 위치를 찾기 ex)
        # ex) 91, 21
        # [1,3,9,27,81,243] -> [1,3,9,27,81,91, 243] 
        # [1,3,9,27] -> [1,3,9,21,27]
        # [1,3,9,27] -> [1,3,9,12,27]
        #2. bisect_left의 idx자리의 값을 다 더한게 41 3^4
        for i in range(c-1, -1, -1):
            temp = n - pow(3, i)
            if temp >= 0:
                n = temp
        
        return n == 0