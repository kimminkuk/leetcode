class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums_dict = {}
        for num in nums1:
            if num[0] not in nums_dict:
                nums_dict[num[0]] = num[1]
            else:
                nums_dict[num[0]] += num[1]
        for num in nums2:
            if num[0] not in nums_dict:
                nums_dict[num[0]] = num[1]
            else:
                nums_dict[num[0]] += num[1]
        answer = []
        for key, value in nums_dict.items():
            answer.append([key,value])
        return sorted(answer, key=lambda x:x[0])