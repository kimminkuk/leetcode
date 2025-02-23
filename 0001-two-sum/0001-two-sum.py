class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums2 = []
        for i, n in enumerate(nums):
            nums2.append((n, i))

        sorted_nums = sorted(nums2, key=lambda x:x[0])
        st, ed = 0, len(sorted_nums)-1
        mid = sorted_nums[st][0] + sorted_nums[ed][0]
        
        while mid != target:
            if mid > target:
                ed -= 1
            if mid < target:
                st += 1
            mid = sorted_nums[st][0] + sorted_nums[ed][0]
        
        return [sorted_nums[st][1], sorted_nums[ed][1]]