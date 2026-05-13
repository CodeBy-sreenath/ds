class Solution:
    def robe(self,nums):
        prev1=0
        prev2=0
        for num in nums:
            current=max(prev1,num+prev2)
            prev2=prev1
            prev1=current
        return prev1
s=Solution()
print(s.robe([1,2,3,1]))        