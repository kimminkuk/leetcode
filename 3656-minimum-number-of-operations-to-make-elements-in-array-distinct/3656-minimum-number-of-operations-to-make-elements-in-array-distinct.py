class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        nums_max = max(nums)
        chk = [0] * (nums_max+1)
        d_multi = {}
        d_sum = 0
        for num in nums:
            chk[num] += 1
            if chk[num] >= 2:
                d_multi[num] = chk[num]
    
        if not d_multi:
            return ans
        chk_num = len(d_multi)
        st, ed = 0, 3
        if ed > len(nums):
            ed = len(nums)
        while st < len(nums):
            ans += 1
            for i in range(st, ed):
                if nums[i] in d_multi:
                    d_multi[nums[i]] -= 1
                    if d_multi[nums[i]] == 1:
                        chk_num -= 1
            if chk_num == 0:
                return ans
            st += 3
            ed += 3
            if ed >= len(nums):
                ed = len(nums)  
        return ans     