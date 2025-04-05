class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = sum(nums)
        for i in range(1, len(nums)):
            for c in itertools.combinations(nums, i+1):
                t = c[0]
                for el in range(1, len(c)):
                    t = t ^ c[el]
                ans += t
                #print(c,t)
        return ans