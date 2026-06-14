function longest(nums)
{
    let longest=0
    let num_set=new Set(nums)
    for(let num of nums)
    {
        if(!num_set.has(num-1))
        {
            let length=1
            while(num_set.has(num+length))
            {
                length+=1
            }
            longest=Math.max(longest,length)
        }
    }
    return longest
}
let nums=[1,2,3,4]
console.log(longest(nums))