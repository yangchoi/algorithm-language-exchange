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
                # 새 계산의 시작
                first = first.next
                first.val = 0
            else:
                # current.val != 0 or current.next == null
                first.val += current.val
            
            if current.next:
                current = current.next
            else:
                # current.next == null
                first.next = None
                break
        return head