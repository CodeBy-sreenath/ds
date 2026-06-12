class Solution:
    def arrayExcept(self,nums):
        n=len(nums)
        prfix=1
        result=[1]*n
        for i in range(n):
            result[i]=prfix
            prfix*=nums[i]
        postfix=1    
        for i in range(n-1,-1,-1):
            result[i] *=postfix
            postfix*=nums[i]
        return result
s=Solution()
nums=[1,2,3,4]
print(s.arrayExcept(nums))        
