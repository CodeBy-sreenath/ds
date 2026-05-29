from collections import deque
class Solution:
    def shortest(self,n,edges):
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist=[-1]*n
        dist[0]=1
        q=deque([0])
        while q:
            node=q.popleft()
            for neighbor in graph[node]:
                if dist[neighbor]==-1:
                    dist[neighbor]=dist[node]+1
                    q.append(neighbor)
        return dist            
s=Solution()
n = 6

edges = [
    [0,1],
    [0,2],
    [1,3],
    [2,4],
    [4,5]
]
print(s.shortest(n,edges))            
