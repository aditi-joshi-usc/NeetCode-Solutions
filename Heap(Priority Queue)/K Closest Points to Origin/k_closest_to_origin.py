class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pqueue = []
        

        for p in points:
            tup = [(p[0] ** 2) + (p[1] ** 2), p[0], p[1]]
            pqueue.append(tup)
        heapq.heapify(pqueue)
        res = []
        while k>0:
            dist, x, y = heapq.heappop(pqueue)
            res.append([x,y])
            k-=1
        return res
