class Solution:
    def isPalindrome(self, x: int) -> bool:
        #1. s to list
        if x < 0: return False
        
        # 1441 -> 1000 + 400 + 40 + 1
        # 1441 % 10 => 1
        # 1441 % 100 => 41 / 10 => 4
        # 1441 % 1000 => 441 / 100 => 4
        # 1441 % 10000 => 1441 / 1000 => 1
        # 1000 -> 1000
        # 1000 % 10 => 0
        # 1000 % 100 => 0 / 10 => 0
        # 1000 % 1000 => 0 / 100 => 0
        # 1000 % 10000 => 1000 / 1000 => 1
        # 10 % 10 => 0
        # 10 % 100 => 10 / 10 => 1
        check = 1
        x_list = []
        while check <= x:
            check *= 10
            x1 = (x % check) / (check / 10)        
            x_list.append(int(x1))
            
        for idx in range(len(x_list) // 2):
            if x_list[idx] != x_list[len(x_list) - idx - 1]: return False
            
        return True