from collections import deque
class Solution:
    def numberofisland(self,grid):
        row=len(grid)
        cols=len(grid[0])
        visit=set()
        island=0
        que=deque()
        
        def bfs(r,c):
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            visit.add((r,c))
            que.append((r,c))
            while que:
                r,c=que.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<row and 0<=nc<cols and grid[nr][nc]=='1' and (nr,nc) not in visit:
                        que.append((nr,nc))
                        visit.add((nr,nc))
        for r in range(row):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    island+=1     
        return island
s=Solution()
grid=[["1","1","1"],["1","1","1"],["0","1","1"]]
print(s.numberofisland(grid))                           



