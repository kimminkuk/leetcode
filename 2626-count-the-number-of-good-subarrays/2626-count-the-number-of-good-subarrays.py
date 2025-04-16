class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        n = len(nums)
        ans = 0
        val = 0
        left = 0
        for right in range(n):
            val += freq[nums[right]]
            freq[nums[right]] += 1

            while val >= k:
                ans += n - right
                freq[nums[left]] -= 1
                val -= freq[nums[left]]
                left += 1
        return ans
