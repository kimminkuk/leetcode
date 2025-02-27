class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # brute-force?

        # 1. nums에서 제일 작은거 구하고 +k
        # 2-1. nums에서 제일 큰 값 - k 범위가 1번 안에 있으면, 무조건 0 가능

        # 2-2. nums에서 제일 큰 값 - k 범위가 1번 안에 없으면, max값을 최대한 줄여서 계산
        nums_min = min(nums)
        nums_max = max(nums)

        nums_min = min(nums) + k
        if (nums_max-k) <= nums_min:
            return 0
        else:
            return (nums_max-k) - nums_min