# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        current = head
        next = head.next
        head.next = None
        while next:
            temp = next
            next = next.next
            temp.next = current
            current = temp
        return current
