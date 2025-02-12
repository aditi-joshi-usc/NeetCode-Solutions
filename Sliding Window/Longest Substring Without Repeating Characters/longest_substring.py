class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res
        char_index = {}

        left = 0
        maxLen = 0
        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]]+1)
            char_index[s[right]] = right
            maxLen = max(maxLen, right-left+1)
        return maxLen
