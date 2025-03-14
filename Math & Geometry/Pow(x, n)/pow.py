class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            n = -n
            x = 1/x

        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        
        if n%2 == 0:
            return self.myPow(x,n/2) * self.myPow(x,n/2)
        else:
            return x * self.myPow(x, n-1)

#Time Complexity = O(logn)
#Space Complexity = O(logn)
