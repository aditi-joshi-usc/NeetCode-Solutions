class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        return None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.min_val[-1] if self.min_val else val, val)
        self.min_val.append(val)
        return None

    def pop(self) -> None:
        self.min_val = self.min_val[:-1]
        self.stack = self.stack[:-1]
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]

        
