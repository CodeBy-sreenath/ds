#Given an integer n, return the least number of perfect square numbers whose sum is n. 
class Solution:
    def squres(self,n):
        squres=[]
        for i in range(1,int(n**0.5)+1):
            squres.append(i**i)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for sq in squres:
                if sq>i:
                    break
                dp[i]=min(dp[i],dp[i-sq]+1)
        return dp[n]
s=Solution()
n=16
print(s.squres(n))                