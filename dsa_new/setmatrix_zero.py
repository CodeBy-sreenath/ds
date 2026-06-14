class Solution:
    def setmatrix(self,matrix):
        row=set()
        col=set()
        r=len(matrix)
        c=len(matrix[0])
        for m in range(r):
            for n in range(c):
                if matrix[m][n]==0:
                    row.add(m)
                    col.add(n)
        for m in range(r):
            for n in range(c):
                if m in row or n in  col:
                    matrix[m][n]=0
        return matrix
s=Solution()
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
print(s.setmatrix(matrix))
