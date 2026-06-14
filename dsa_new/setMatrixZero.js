function setMatrix(matrix)
{
    let row=new Set()
    let col=new Set()
    let r=matrix.length
    let c=matrix[0].length
    for(let i=0;i<r;i++)
    {
        for(let j=0;j<c;j++)
        {
            if(matrix[i][j]==0)
            {
                row.add(i)
                col.add(j)
            }
        }
    }
    for(let i=0;i<r;i++)
    {
        for(let j=0;j<c;j++)
        {
            if(row.has(i) || col.has(j))
            {
                matrix[i][j]=0
            }
        }
    }
    return matrix;
}
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
console.log(setMatrix(matrix))