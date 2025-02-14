class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time Complexity = O(n^2 log n)
        # Space Complexity = O(1) or O(n) based on the sorting algorithm
        # stones.sort(reverse = False)
        # res = 0
        # while stones:
        #     stone1 = stones.pop()
        #     if not stones:
        #         return stone1
        #     stone2 = stones.pop()
            
        #     res = stone1-stone2
        #     stones.append(res)
        #     stones.sort(reverse=False)
            
        # return res


        #Time Complexity = O(nlogn)
        #Space Complexity = O(n)
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone2 > stone1:
                heapq.heappush(stones, stone1-stone2)
        stones.append(0)
        return abs(stones[0])


        
