function fibanocci(n)
{
    let a=0
    let b=1
    for(let i=0;i<n;i++)
    {
        console.log(a)
        c=a+b
        a=b
        b=c

    }
}
console.log(fibanocci(6))