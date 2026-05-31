class Solution:
    def merge(self,intervels):
        intervels.sort(key=lambda x:x[0])
        result=[intervels[0]]
        for start,end in intervels[1:]:
            last_end=result[-1][1]
            if start<=last_end:
                result[-1][1]=max(last_end,end)
            else:
                result.append([start,end]);
        return result
s=Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]));              