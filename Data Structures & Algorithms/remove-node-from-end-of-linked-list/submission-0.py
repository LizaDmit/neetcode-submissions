# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head

        if n == 1:
            return None

        for i in range (n):
            prev = cur
            cur = cur.next
        
        prev.next = cur.next
        cur.next = None

        return head