class Solution:
    def __init__(self):
        self.res = "1"
    def countAndSay(self, n: int) -> str:
        def recur(n, nums):
            if n < 1:
                return
            
            prev = nums[0]
            cnt = 1
            ans = ""
            for num in nums[1:]:
                if num != prev:
                    ans += (str(cnt) + prev)
                    cnt = 1
                    prev = num
                else:
                    cnt += 1
                    
            ans += (str(cnt)+prev)
            self.res = ans
            recur(n-1, ans)
        
        recur(n-1, "1")
        return self.res        