class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # heap으로 최소 값 구하고
        # i 순회 하면서, 최소 값과 일치하는 element 값에 곱하기
        # k만큼 반복
        # heap이나 min 이나 똑같지 않나...

        for k_idx in range(k):
            cur_min = min(nums)
            for idx, el in enumerate(nums):
                if el == cur_min:
                    nums[idx] = nums[idx] * multiplier
                    break
        return nums