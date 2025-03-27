class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        
        dq = deque([source])
        visited = [False for _ in range(n)]
        ans = False
        while dq:
            st = dq.popleft()
            if st == destination:
                ans = True
                break
            if visited[st] != True:   
                visited[st]=True             
                for value in d[st]:
                    dq.append(value)
        
        return ans