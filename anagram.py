class Solution:
    def anagram(self,s,t):
        if len(s)!=len(t):
            return False
        count={}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1 
            if count[ch] <0:
                return False
        return True
s=Solution()
print(s.anagram("anagram", "nagaram"))
print(s.anagram("rat", "car"))                   