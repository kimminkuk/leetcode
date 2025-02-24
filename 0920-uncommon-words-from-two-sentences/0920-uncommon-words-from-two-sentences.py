class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_split, s2_split = s1.split(), s2.split()
        d = {}
        for s1_s in s1_split:
            if s1_s not in d:
                d[s1_s] = 1
            else:
                d[s1_s] += 1
        
        for s2_s in s2_split:
            if s2_s not in d:
                d[s2_s] = 1
            else:
                d[s2_s] += 1
        
        answer = []
        for key in d.keys():
            if d[key] == 1:
                answer.append(key)
            
        
        return answer        