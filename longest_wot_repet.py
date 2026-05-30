class Solution:
    def longest(self,s):
        left=0
        max_len=0
        seen=set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[right])
                left+=1
            seen.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
obj=Solution()
s="abcabcbb"
print(obj.longest(s))            
            