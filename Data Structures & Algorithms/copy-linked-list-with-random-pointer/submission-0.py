"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        oldTocur ={None:None}
        while cur:
            copy = Node(cur.val)
            oldTocur[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            node = oldTocur[cur]
            node.next = oldTocur[cur.next]
            node.random = oldTocur[cur.random]
            # oldTocur[cur] = node
            cur = cur.next
        return oldTocur[head]
