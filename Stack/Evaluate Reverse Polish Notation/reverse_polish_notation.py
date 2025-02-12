class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        if not tokens:
            return 0

        for token in tokens:
                           
            if token == '+':
                temp =  stack.pop()
                temp +=  stack.pop()
                stack.append(temp)
            elif token == '-':
                temp =  stack.pop()
                temp =  stack.pop() - temp
                stack.append(temp)
            elif token == '*':
                temp =  stack.pop()
                temp =  stack.pop() * temp
                stack.append(temp)
            elif token == '/':
                temp =  stack.pop()
                temp =  int((stack.pop())/temp)
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack.pop()

        
