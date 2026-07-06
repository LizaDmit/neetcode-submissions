# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = head
        head2 = slow.next
        slow.next = None

        prevNode = None
        curNode = head2

        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        
        p1 = head
        p2 = prevNode

        while p1 and p2:
            nextt1 = p1.next
            nextt2 = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = nextt1
            p2 = nextt2

    
            
        

