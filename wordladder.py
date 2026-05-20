from collections import deque
class Solution:
    def wordladder(self,beginword,endword,wordlist):
        wordset=list(wordlist)
        que=deque()
        visited=set()
        que.append([beginword,1])
        visited.add(beginword)
        if endword not in wordset:
            return 0
        while que:
            word,level=que.popleft()
            if word==endword:
                return level
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword=word[:i]+ch+word[i+1:]
                    if newword in wordset and newword not in visited:
                        visited.add(newword)
                        que.append((newword,level+1))
        return 0
s=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(s.wordladder(beginWord,endWord,wordList))                    


