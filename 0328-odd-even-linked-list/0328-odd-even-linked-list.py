class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None: return None
        if head.next is None: return head

        first = head
        current = head.next
        evenHead = current

        while current.next is not None:
            first.next = current.next
            current.next = current.next.next

            first = first.next
            current = current.next

            if current is None: break

        first.next = evenHead
        return head