# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        count = 0
        while count < 3:
            if p1 is p2:
                return p1
            if p1 and p1.next:
                p1 = p1.next
            else:
                count += 1
                p1 = headB
            if p2 and p2.next:
                p2 = p2.next
            else:
                count += 1
                p2 = headA
