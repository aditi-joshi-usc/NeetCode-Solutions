class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u1, v1, w1 in times:
            edges[u1].append((v1, w1))

        #node, path_cost
        minHeap = [(0, k)]

        heapq.heapify(minHeap)
        final_cost = 0
        visited = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)
            final_cost = cost
            
            #bfs
            for v1, t1 in edges[node]:
                if v1 not in visited:
                    heapq.heappush(minHeap, (t1+cost, v1))
                

        return final_cost if len(visited) == n else -1

        #Time Complexity = O(ELogV) E: Edges, V: nodes
