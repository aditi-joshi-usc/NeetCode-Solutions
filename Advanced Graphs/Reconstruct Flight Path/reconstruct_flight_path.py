class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map_ticket = defaultdict(list)
        tickets.sort()
        for ticket in tickets:
            map_ticket[ticket[0]].append(ticket[1])

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in map_ticket:
                return False

            temp = map_ticket[src]
            for i, dest in enumerate(temp):
                map_ticket[src].pop(i)

                res.append(dest)

                if dfs(dest) :
                    return True
                map_ticket[src].insert(i, dest)
                res.pop()
            return False
        
        dfs('JFK')
        return res
                  

