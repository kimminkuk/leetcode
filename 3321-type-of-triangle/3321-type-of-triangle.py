class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums_sorted = sorted(nums)
        def check_triangle(check_nums):
            if check_nums[0] + check_nums[1] > check_nums[2]:
                return True
            return False
        
        answer_list = ["equilateral", "isosceles", "scalene", "none"]
        if check_triangle(nums_sorted):
            nums_counter = Counter(nums_sorted)
            return answer_list[len(nums_counter)-1]
        else:
            return answer_list[3]