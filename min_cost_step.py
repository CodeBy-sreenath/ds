#minimum cost required for covering the steps
class Solution:
    def min_cost(self,cost):
        n=len(cost)
        first=cost[0]
        second=cost[1]
        for i in range(2,n):
            current=cost[i]+min(first,second)
            first=second
            second=current
        return min(first,second)
s=Solution()
print(s.min_cost([1,100,1,1,100,1,1,100,1]))        
    
    
    