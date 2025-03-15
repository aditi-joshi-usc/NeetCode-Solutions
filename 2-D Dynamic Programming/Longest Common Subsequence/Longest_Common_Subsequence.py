class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if text1  == text2:
            return len(text1)
        
        if len(text1) < len(text2):
            text1, text2 = text2, text1


        prev = [0 for j in range(len(text2)+1)]
        curr = [0 for j in range(len(text2)+1)]


        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2)-1, -1, -1):

                if text1[i] == text2[j]:
                    curr[j] = 1+ prev[j+1]
                else:
                    curr[j] = max(prev[j], curr[j+1])
            prev,curr = curr, prev

        
        
        return prev[0]
#Time complexity = O(m*n)
#Space complexity = O(min(m,n)) 
