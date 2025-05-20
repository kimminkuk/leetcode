class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        answer = [words[0]]
        sequence_flag = groups[0]
        for word, group in zip(words[1:], groups[1:]):
            if sequence_flag != group:
                answer.append(word)
            sequence_flag = group
        return answer
