class Solution:
    def besttime(self,nums):
        min_price=float('inf')
        max_profit=0
        for num in nums:
            min_price=min(num,min_price)
            max_profit=max(max_profit,num-min_price)
        return max_profit
s=Solution()
nums=[7, 1, 5, 3, 6, 4];
print(s.besttime(nums))        