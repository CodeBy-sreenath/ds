from collections import deque
class Solution:
    def provience(self,grid):
        que=deque()
        visited=set()
        provience=0
        n=len(grid)
        def bfs(city):
            que.append(city)
            visited.add(city)
            while que:
                city=que.popleft()
                for neighbor in range(n):
                    if grid[city][neighbor]==1 and neighbor not in visited:
                        visited.add(neighbor)
                        que.append(neighbor)
           

        for city in range(n):
            if city  not in visited:
                 bfs(city)
                 provience+=1
        return provience         
s=Solution()
grid= [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(s.provience(grid))                 
                   

