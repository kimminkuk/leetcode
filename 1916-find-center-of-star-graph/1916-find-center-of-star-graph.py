class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        n = len(edges)

        for i in range(n+1):
            if i+1 not in d:
                d[i+1]=0

        for edge in edges:
            #print(edge)
            d[edge[0]]+=1
            d[edge[1]]+=1
            #print(d)
        
        #print(n, d)
        ans = 0
        for key, value in d.items():
            if value == n:
                ans = key
        return ans