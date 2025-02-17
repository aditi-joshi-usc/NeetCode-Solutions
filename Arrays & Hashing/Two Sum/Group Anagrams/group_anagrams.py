class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Sorting - Time Complexity = O(m * nlogn)
        # res = defaultdict(list)

        # for s in strs:

        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)

        # return list(res.values)



        #Hashmap - Time Complexity = O(n * m * 26) = O(n * m)

        res = defaultdict(list)

        for s in strs:


            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())
