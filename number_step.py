#the number of ways to climb n stairs when you can climb either 1 or 2 steps at a time
class Solution:
    def climbStairs(self,n):
        if n<=2:
            return n
        left=1
        right=2
        for i in range(3,n+1):
            current=left+right
            left=right
            right=current
        return right
s=Solution()
print(s.climbStairs(5))        