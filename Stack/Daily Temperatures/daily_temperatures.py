class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        res = [0]*len(temperatures)

        stack=[0]

        for i in range(len(temperatures)):

            while stack!=[] and temperatures[i] > temperatures[stack[-1]]:

                indx = stack.pop()

                res[indx] = i-indx 
            stack.append(i)

        return res
