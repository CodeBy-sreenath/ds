class Solution:
    def longest(self,nums):
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
s=Solution()
nums=[10,9,2,5,3,7,108]
print(s.longest(nums))
