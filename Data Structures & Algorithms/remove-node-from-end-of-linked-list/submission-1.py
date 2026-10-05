# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left, right = dummy,head
        for i in range(n):
            if right:
                right = right.next
            else:
                return None
        while right:
            left = left.next
            right =right.next
        prev = left
        prev.next = prev.next.next
        return dummy.next