class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        states = [0] * numCourses
        unseen = 0
        visiting = 1
        visited = 2

        track = defaultdict(list)
        if len(prerequisites) == 0:
            return True

        for a,b in prerequisites:
            track[a].append(b) 

        def dfs(course):
            state = states[course]
            
            if state == 2:
                return True
            
            if state == 1:
                return False
            
            states[course] = visiting
            for i in track[course]:
                if not dfs(i):
                    return False
            states[course] = visited
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        
        
