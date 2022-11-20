# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        current = head.next
        while current:
            if current.val == 0 and current.next:
                first = first.next
                first.val = 0
            else:
                first.val += current.val
            
            if current.next:
                current = current.next
            else:
                first.next = None
                break
        return head