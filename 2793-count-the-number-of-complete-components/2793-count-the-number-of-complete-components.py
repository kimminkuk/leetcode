class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        freq = defaultdict(int)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        for i in range(len(graph)):
            graph[i].append(i)
            freq[i] = tuple(sorted(graph[i]))
    
        
        d = {}
        for key, value in freq.items():
            if value not in d:
                d[value] = 1
            else:
                d[value] += 1
        
        ans = 0
        for key, value in d.items():
            if len(key) == value:
                ans += 1    
        
        return ans