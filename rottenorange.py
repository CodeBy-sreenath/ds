from collections import deque
class Solution:

    def rotten(self,grid):
        row=len(grid)
        cols=len(grid[0])
        que=deque()
        fresh=0
        minute=0
        for r in range(row):
            for c in range(cols):
                if grid[r][c]==2:
                    que.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1    
        if fresh==0:
            return 0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while que and fresh>0:
            for i in range(len(que)):
                r,c=que.popleft()
                for dr,dc in directions:
                    nr=dr+r
                    nc=dc+c
                    if 0<=nr<row and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        que.append((nr,nc))
            minute+=1
        if fresh>0:
            return -1
        return minute
s=Solution()
grid=[[2,1,2],[1,1,0],[0,1,1]]
print(s.rotten(grid))                    

