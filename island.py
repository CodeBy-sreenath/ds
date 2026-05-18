class Solution:
    def numberofisland(self,grid):
        row=len(grid)
        cols=len(grid[0])
        visit=()
        island=0
        def bfs(r,c):
