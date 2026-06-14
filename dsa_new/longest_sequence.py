class Solution:
    def longest(self,nums):
        num_set=set(nums)
        logest=0
        for num in nums:
            if num-1 not in num_set:
                length=1
                while num+length in num_set:
                    length+=1
                logest=max(logest,length)
        return logest
s=Solution()
nums=[1,2,3,4]
print(s.longest(nums))