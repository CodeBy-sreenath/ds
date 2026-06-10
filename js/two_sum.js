function twoSum(nums,target)
{
    const seen={}
    for(let i=0;i<nums.length;i++)
    {
        const complement=target-nums[i]
        if(complement in seen)
        {
            return [seen[complement],i]
        }
        seen[nums[i]]=i
    }
}
const nums = [2, 7, 11, 15];
const target = 9;

console.log(twoSum(nums, target));