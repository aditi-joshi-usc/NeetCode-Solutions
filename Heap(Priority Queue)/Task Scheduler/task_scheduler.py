class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count= [0] * 26

        for t in tasks:
            count[ord(t) - ord('A')] +=1
        
        maxheap = []

        for i in count:
            if i != 0:
                maxheap.append(-i)

        heapq.heapify(maxheap)

        time = 0
        q = deque() #[-cnt, idleTime]

        while maxheap or q:
            time+=1

            if not maxheap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxheap)
                cnt = cnt+1  #deduct 1 from the -ve cnt
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time


#Time Complexity = O(m*n) where n is the number of tasks, an m is the idle time
