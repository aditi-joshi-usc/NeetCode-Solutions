class Solution:
    def hammingWeight(self, n: int) -> int:
        # res=0
        # while n:
        #     res += n%2
        #     n= n>>1 # move bits to right

        # return res

        res = 0
        while n:
            n = n & (n-1)
            res+=1
        return res
