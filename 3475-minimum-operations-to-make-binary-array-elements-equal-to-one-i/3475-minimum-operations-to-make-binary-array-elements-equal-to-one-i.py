class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        
        
        # 0) 0 1 1 1 0 0
        # 1) 0 1 1 0 1 1
        # 2) 0 0 0 1 1 1
        # 3) 1 1 1 1 1 1
        
        # challenge1) reverse 
        ans = 0
        while right > 1:
            if nums[right] == 0:
                nums[right-2 : right+1] = [x ^ 1 for x in nums[right-2 : right+1]]
                ans += 1
            right -= 1
        
        
        if n != sum(nums):
            return -1
                
        return ans        