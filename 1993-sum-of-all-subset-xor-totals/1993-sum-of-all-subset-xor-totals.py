class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def sub(ori, subset, index, subsets):
            subsets.append(subset[:])
            for i in range(index, len(ori)):
                subset.append(ori[i])
                sub(ori, subset, i+1, subsets)
                subset.pop()
            return
        subsets = []
        sub(nums, [], 0, subsets)
        ans = 0
        for subset in subsets:
            r1 = 0
            for el in subset:
                r1 ^= el
            ans += r1
        return ans
        