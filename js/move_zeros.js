function moveZero(nums)
{
    let pos=0
    for(let i=0;i<nums.length;i++)
    {
        if(nums[i]!=0)
        {
            [nums[i],nums[pos]]=[nums[pos],nums[i]]
            pos++
        }
    }
    return nums
}
console.log(moveZero([0,1,0,3,12]))