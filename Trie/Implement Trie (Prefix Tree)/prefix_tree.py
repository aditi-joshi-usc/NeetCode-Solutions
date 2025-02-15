class Node:

    def __init__(self):
        self.children = {}
        self.isEndofWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w in curr.children:
                curr = curr.children[w]
            else:
                curr.children[w] = Node()
                curr = curr.children[w]
        curr.isEndofWord = True 



    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w in curr.children:
                curr = curr.children[w]
            else:
                return False
        return curr.isEndofWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w in curr.children:
                curr = curr.children[w]
            else:
                return False
        return True
        
