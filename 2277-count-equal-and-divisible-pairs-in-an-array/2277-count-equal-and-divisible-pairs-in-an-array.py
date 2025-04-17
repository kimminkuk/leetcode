class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq_key = defaultdict(list)
        ans = 0
        for i, el in enumerate(nums):
            for j in freq_key[el]:
                if (i * j) % k == 0:
                    ans += 1           
            freq_key[el].append(i)
        return ans