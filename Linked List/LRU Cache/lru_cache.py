class Node:
    def __init__(self, key= -1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1, None, None)

        self.tail = Node(-1, -1, None, self.head)

        self.head.next = self.tail

        self.capacity = capacity
        self.used_capacity = 0
        self.track = {}

    def get(self, key: int) -> int:

        node = self.head

        
        if key in self.track:
            getnode = self.remove(self.track[key])
            self.add(getnode)
            return getnode.val
      
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            getnode = self.remove(self.track[key])
            getnode.val = value
        
        else:
            getnode = Node(key, value, None, None)
            self.used_capacity +=1
        
        self.add(getnode)
        if self.used_capacity > self.capacity:
            temp = self.head.next
            self.remove(temp)
            self.used_capacity-=1
            
        
        
        
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.track[node.key]
        return node
    
    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.track[node.key] = node


        
        
        
    


        
