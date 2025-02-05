class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        for character in s:
            if character.isalnum():
                ans+=character.lower()
        return ans == ans[::-1]



