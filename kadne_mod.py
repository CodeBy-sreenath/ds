class Solution:
    def maxSubArray(self,nums):
        current_sum=nums[0]
        max_sum=nums[0]
        start=temp_start=end=0
        for i in range(1,len(nums)):
            if nums[i] > nums[i]+current_sum:
                current_sum=nums[i]
                temp_start=i
            else:
                current_sum+=nums[i]
            if current_sum>max_sum:
                max_sum=current_sum
                start=temp_start
                end=i
        return max_sum,nums[start:end+1];
s=Solution()    

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


max_sum, subarray =s. maxSubArray(nums)

print("Maximum Sum:", max_sum)
print("Subarray:", subarray)    
                    

