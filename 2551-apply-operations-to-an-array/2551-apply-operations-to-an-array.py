class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        nums_copy = nums.copy()
        for i, num in enumerate(nums[:-1]):
            if nums_copy[i] == nums_copy[i+1]:
                nums_copy[i] *= 2
                nums_copy[i+1] = 0
        
        ans = []
        for num in nums_copy:
            if num != 0:
                ans.append(num)
        temp = nums_len - len(ans)
        ans = ans + [0] * temp
        return ans