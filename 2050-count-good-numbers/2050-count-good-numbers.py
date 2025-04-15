class Solution:
    MOD=10**9+7
    def speed_cal_of_pow(self, base, power):
        result = 1
        base %= self.MOD
        while power > 0 :
            if power % 2 == 1:
                result = (result * base) % self.MOD
            base = (base * base) % self.MOD
            power //= 2
        return result

    def countGoodNumbers(self, n: int) -> int:
        mul_5, mul_4 = (n+1)//2, n//2        
        return (self.speed_cal_of_pow(5, mul_5) * self.speed_cal_of_pow(4, mul_4)) % self.MOD
