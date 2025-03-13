class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i] == True:
                    break
        return dp[0]

        #Time Complexity = O(len(s) * len(word_dict) * max_len of word in dict) = O(n*m*t)
        #Space Complexity = O(n)



# Using Hashset
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        words = set(wordDict)
        dp[0] = True

        for i in range(1, (n+1)):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]

#Time Complexity = O(n^2)
#Space Complexity = O(n)
