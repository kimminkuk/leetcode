class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        #??어제랑 똑같은거같은데
        n = len(nums)
        left = n * [0]
        right = n * [0]

        for i in range(1,n):
            left[i] = max(left[i-1], nums[i-1])
            right[n-1-i] = max(right[n-i], nums[n-i])

        ans = 0
        for i in range(1, n):
            ans = max(ans, (left[i]-nums[i])*right[i] )
        return ans