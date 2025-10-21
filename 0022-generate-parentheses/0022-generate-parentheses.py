class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back_tracking(parth, left, right):
            if left == n and right == n:
                result.append(parth)
                return
            if left < n:
                back_tracking(parth + "(", left + 1, right)
            if left > right:
                back_tracking(parth + ")", left, right + 1)
        result = []
        back_tracking("", 0, 0)
        return result