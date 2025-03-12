class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        visited = 2
        visiting = 1
        unseen = 0
        states = [0] * numCourses

        track = defaultdict(list)

        for a, b in prerequisites:
            track[a].append(b)



        def dfs(node):
            state = states[node]

            if state == visiting:
                return False
            if state == visited:
                return True
            
            states[node] = visiting

            for i in track[node]:
                if not dfs(i):
                    return False
            states[node] = visited
            res.append(node)
        
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

        
