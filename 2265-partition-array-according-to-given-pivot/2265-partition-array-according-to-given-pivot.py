class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #1. pivot index 위치 찾기 
        #2. num 순회하면서, pivot 기준 왼쪽 오른쪽 나눠서 append 해두기
        #3. lefts=[9,5,3], rights=[12,14], equals=[10,10]
        #         [0,2,5]  [3,6] [1,4]
        # 0->0, 2->1, 5->2, 3->3, 6->4, 7->1, 8->4
        #4. 1번 위치 기준으로 lefts, equals, rights 넣기?
        
        # pivot 위치 index:3  -> position은 4

        # lefts=[-3], rights=[4,3], equals=[2]
        # 
        lefts,rights,equals=[],[],[]
        nums_copy = nums.copy()
        for i, num in enumerate(nums):
            if pivot == num:
                equals.append(i)
            elif pivot > num:
                lefts.append(i)
            else:
                rights.append(i)
        
        alls = lefts + equals + rights
        i = 0
        for idx in alls:
            nums[i] = nums_copy[idx]
            i += 1
        return nums


