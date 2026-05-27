class Solution:
    def freq_set(self,s,k):
        
        result=set()
        for i in range(len(s)):
            freq={}
            for j in range(i,len(s)):
                ch=s[j]
                if ch in freq:
                    freq[ch]+=1
                else:
                    freq[ch]=1
                if len(freq)==k:
                    result.add(s[i:j+1])
                if len(freq)>k:
                    break
        return len(result)
st=Solution()
s="pqps"
k=2
print(st.freq_set(s,k))                
