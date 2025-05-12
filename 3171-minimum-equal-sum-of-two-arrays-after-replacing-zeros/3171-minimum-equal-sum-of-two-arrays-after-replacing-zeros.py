class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # 0 개수 찾기
        # 0 제외 합  찾기
        def get_sum_and_zero_cnt(arr):
            _sum, _cnt = 0, 0
            for el in arr:
                _sum += el
                if el == 0:
                    _cnt += 1
            return _sum, _cnt
        nums1_sum, nums1_zero_cnt = get_sum_and_zero_cnt(nums1)
        nums2_sum, nums2_zero_cnt = get_sum_and_zero_cnt(nums2)
        if (nums1_sum+nums1_zero_cnt) > nums2_sum and nums2_zero_cnt == 0:
            print('this?')
            return -1
        if (nums2_sum+nums2_zero_cnt) > nums1_sum and nums1_zero_cnt == 0:
            print('this?-2')
            return -1
    
        return max(nums1_sum+nums1_zero_cnt, nums2_sum+nums2_zero_cnt)