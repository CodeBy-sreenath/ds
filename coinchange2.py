#the number of ways that the coin can be  selected to achieve the target amount
class Solution:
    def change(self,costs,amount):
        dp=[0]*(amount+1)
        dp[0]=1
        for cost in costs:
            for i in range(cost,amount+1):
                dp[i]+=dp[i-cost]
        return dp[amount]
s=Solution()            
costs=[1,2,5]
amount=5
print(s.change(costs,amount))
