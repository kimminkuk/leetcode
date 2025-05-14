import itertools
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        freq = Counter(digits)
        for i in range(100, 1000, 2):
            a = []
            for s in str(i):
                a.append(int(s))
            freq1 = Counter(a)
            chk = 1
            for key in freq1.keys():
                if freq[key] >= freq1[key]:
                    chk *= 1
                else:
                    chk *= 0
            if chk == 1:
                res.append(i)
        return res