class Solution:
    def remove(self,nums):
        arr=[]
        for num in nums:
            if num not in arr:
                arr.append(num)
        return arr
s=Solution()
nums=[1,2,1,3,2,4,5]
print(s.remove(nums))            