class Solution:
    def greatest(self,nums):
        greatest_element=nums[0]
        for num in nums:
            if num>greatest_element:
                greatest_element=num
        return greatest_element
s=Solution()
nums=[1,6,8,9,0]
print(s.greatest(nums))            