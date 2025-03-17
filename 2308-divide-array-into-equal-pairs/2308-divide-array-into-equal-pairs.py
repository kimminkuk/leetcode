class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        pair_n = len(nums) // 2
        pair_count = 0
        for key, value in d.items():
            if value % 2 == 0:
                pair_count += value // 2
        
        
        return pair_n == pair_count        