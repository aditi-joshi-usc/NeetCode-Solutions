class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #heap Time complexity  = O(klogn)
        # dict1 = defaultdict(int)

        # for i in nums:
        #     dict1[i] +=1
        
        # stack = []
        # for key, value in dict1.items():
        #     stack.append((-value, key))
        
        # heapq.heapify(stack)

        # ans = []
        # while k>0:
        #     ans.append(heapq.heappop(stack)[1])
        #     k-=1
        # return ans

        #Bucket Sort Time complexity  = O(n)

        dict1 = defaultdict(int)

        for i in nums:
            dict1[i] +=1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in dict1.items():
            freq[value].append(key)
        
        res = []

        for i in range(len(freq)-1,0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
       
