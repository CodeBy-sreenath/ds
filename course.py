from collections import defaultdict
class Solution:
    def courseschedule(self,numCourse,prerequisite):
        graph=defaultdict(list)
        for course,prereq in prerequisite:
            graph[prereq].append(course)
            state=[0]*numCourse
            def dfs(course):
                if state[course]==1:
                    return False
                if state[course]==2:
                    return True
                state[course]=1
                for neighbor in graph[course]:
                    if not dfs(neighbor):
                        return False
                state[course]=2
                return True    
                




            for course in range(numCourse):
                if not dfs(course):
                    return False
        return True
s=Solution()
numCourse=4
prerequisite=[[1, 0],  # 0 → 1
    [2, 1],  # 1 → 2
    [3, 2] ]  # 2 → 3]            
print(s.courseschedule(numCourse,prerequisite))
