class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while True:
            s = 0
            while n!=0:
                s = s+ math.pow(n%10, 2)
                n = n//10
            if s==1:
                return True
            elif s in track:
                return False
            else:
                n = s
                track.add(s)
