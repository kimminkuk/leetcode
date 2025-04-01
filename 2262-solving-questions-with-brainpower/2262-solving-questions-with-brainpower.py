class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        data = [-1] * len(questions)
        def recur(i):
            if i >= len(questions):
                return 0
            
            if data[i] != -1:
                return data[i]

            data[i] = max(questions[i][0] + recur(questions[i][1]+i+1), recur(i+1))
            
            return data[i]

        
        return recur(0)