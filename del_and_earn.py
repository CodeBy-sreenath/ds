class Solution:
    def deleteandEarn(self,nums):
        max_nums=max(nums)
        points=[0]*(max_nums+1)
        for num in nums:
            points[num]+=num
        prev1=0
        prev2=0
        for value in points:
            current=max(prev1,value+prev2)
            prev2=prev1
            prev1=current
        return prev1
s=Solution()
print(s.deleteandEarn([2,3,4]))            