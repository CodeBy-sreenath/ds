#how many coins will be selected for reach the minimum amount
class Solution:
    def minimumcost(self,costs,amount):
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for cost in costs:
                if i>=cost:
                    dp[i]=min(dp[i],dp[i-cost]+1)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
s=Solution()
costs=[1,2,5]
amount=11
print(s.minimumcost(costs,amount));                
            