class Solution:
    def longest(self,st):
        left=0
        seen=set()
        max_length=0
        for right in range(len(st)):
            while st[right] in seen:
                seen.remove(st[left])
                left+=1
            seen.add(st[right])
            max_length=max(max_length,right-left+1)
        return max_length
s=Solution()
st="abcabcbbbbhjklmnop"
print(s.longest(st))
            