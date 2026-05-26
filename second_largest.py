class Solution:
    def second_largest(self,nums):
        greatest_element=float('-inf')
        second_greatest=float('-inf')
        for num in nums:
            if num>greatest_element:
                second_greatest=greatest_element
                greatest_element=num
            if num>second_greatest and num!=greatest_element:
                second_greatest=num
        return second_greatest
s=Solution()
nums=[9,6,8,7,2]
print(s.second_largest(nums))  ;              