class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        visited = set()
        if len(edges) > (n-1):
            return False

     


        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)



        def dfs(node, parent):
            
            if node in visited:
                return False
            visited.add(node)
            for i in adj[node]:
                if i == parent:
                    continue
                
                if not dfs(i, node):
                    return False
            return True

        
        return dfs(0, -1) and len(visited) == n

        #Time Complexity = O(V+E)
        #Space Complexity = O(V+E)
