# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        carry = 0 # 올림자리 보관

        while l1 or l2 or carry:
            current.next = ListNode()
            current = current.next
            num1 = num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            current.val = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10
        return result.next