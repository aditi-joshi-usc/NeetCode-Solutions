class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0 
        adj = [[] for _ in range(n)]

        for start, end, price in flights:
            adj[start].append([end,price])



        
        q = deque([(0,src, 0)])
         # price_till_now, src, stops

       
        

        while q:
            price_till_now, start, kk = q.popleft()
            if kk > k:
                continue
            
            
            for end, cost in adj[start]:
                next_price = price_till_now + cost
                if next_price < prices[end]:
                    prices[end] = next_price
                    q.append((next_price, end, kk+1))
        
        if prices[dst] != float('inf'):
            return prices[dst]
        else:
            return -1

        # Time Complexity = O(number of cities  * number of stops)
        # Space complexity = O(number of cities + number of flights)
