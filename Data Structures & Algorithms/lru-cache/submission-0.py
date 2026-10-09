class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.key = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def _insert(self,node:Node):
        prev,next = self.right.prev,self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def _remove(self,node:Node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev
        

    def get(self, key: int) -> int:
        if key not in self.key:
            return -1
        node = self.key[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key:
            self._remove(self.key[key])
        node = Node(key,value)
        self._insert(node)
        self.key[key]=node
        
        if len(self.key)>self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.key[lru.key]


