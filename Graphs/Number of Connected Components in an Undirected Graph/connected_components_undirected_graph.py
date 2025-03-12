class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        
        def dfs(node, parent):
            if node in visited:
                return 
            visited.add(node)
            for i in adj[node]:
                if i == parent:
                    continue
                dfs(i, node)
                    

        count = 0

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count+=1
        return count
        #Time Complexity = O(V+E)
        #Space complexity= O(V+E)


        
