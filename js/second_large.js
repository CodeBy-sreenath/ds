function secondLargest(num)
{
    let first=-1
    let second=-1
    for(let i of num)
    {
        if(num>first)
        {
            second=first
            first=i
        }
        else if(i>second && i!==first)
        {
            second=i
        }
    }
    return second
}
console.log(secondLargest([1,3,6,7,0,8]))