# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = ListNode(0)
        dummy.next = cur
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            temp = v1 + v2 + carry
            current = temp%10
            carry = temp//10
            cur.val = current

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if l1 or l2 or carry:
                cur.next = ListNode(0)
                cur = cur.next
            
        return dummy.next
            