class Solution:
    def isValid(self, s: str) -> bool:
        paran_dict = {')': '(', ']': '[', '}': '{'}

        stack = []

        for character in s:
                        
            if character in paran_dict:
                if len(stack) !=0 and stack[-1] == paran_dict[character]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(character)


        return len(stack) == 0




        
