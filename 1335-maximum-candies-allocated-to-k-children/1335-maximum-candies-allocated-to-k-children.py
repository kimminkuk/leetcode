class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candy = max(candies)
        ans = 0
        left, right = 0, max_candy
        
        while left < right:
            mid = (left+right+1)//2
            max_candy = 0
            for candy in candies:
                max_candy += (candy//mid)
            if max_candy >= k:
                ans = mid
                left = mid
            else:
                right = mid-1

        return ans