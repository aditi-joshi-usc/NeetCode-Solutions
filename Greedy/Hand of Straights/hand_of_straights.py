class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
       
        # if len(hand) % groupSize != 0:
        #     return False
        

        # hand.sort()
        
        # count = Counter(hand)

        # for num in hand:
        #     if count[num]:
        #         for i in range(num, num+groupSize):
        #             if not count[i]:
        #                 return False
        #             count[i] -=1
        # return True

    #Time complexity = O(nlogn)


        if len(hand) % groupSize != 0:
            return False
        

        count = defaultdict(int)

        for num in hand:
            count[num]+=1
        
        minhList = list(count.keys())
        heapq.heapify(minhList)


        while minhList:
            minh = minhList[0]

            for i in range(minh, minh + groupSize):
                if not count[i]:
                    return False
                count[i] -=1
                if count[i] == 0:
                    if i != minhList[0]: # if count is 0 and it is not the min value then false
                        return False
                    heapq.heappop(minhList)
        return True
        
# Time complexity = O(nlogn)
#Space Complexity = O(n)
