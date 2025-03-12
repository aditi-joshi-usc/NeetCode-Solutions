class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0


        for i in range(len(s)):
            self.count_palindrome(s, i, i)
            self.count_palindrome(s, i, i+1)
        return self.res

    def count_palindrome(self, s, l,r):

        while l>=0 and r< len(s) and s[l] == s[r]:
            self.res+=1
            l-=1
            r+=1
    #Time Complexity = O(n^2)
    #Space Complexity = O(1) 
