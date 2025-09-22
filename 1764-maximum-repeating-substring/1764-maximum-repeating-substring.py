class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 이전 문제는, aaaa등의 예외처리가 불가
        repeated_word = word
        answer = 0
        while repeated_word in sequence:
            answer += 1
            repeated_word += word
        return answer
