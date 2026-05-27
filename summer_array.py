class Solution:
    def summer(self,nums):
        left=0
        right=len(nums)-1
        swap=0
        while left<right:
            while left<right and nums[left]%2==1:
                left+=1
            while left<right and nums[right]%2==0:
                right-=1
            if left<right:
                nums[left],nums[right]=nums[right],nums[left]
                swap+=1
        return swap
s=Solution()
nums=[2, 4, 1, 3, 6, 5]  
print(s.summer(nums))             