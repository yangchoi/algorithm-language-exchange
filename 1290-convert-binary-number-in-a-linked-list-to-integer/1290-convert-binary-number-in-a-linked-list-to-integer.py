# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bit_numbers = []
        
        while head is not None:
            bit_numbers.append(str(head.val))
            head = head.next
        bit_number = ''.join(bit_numbers)
        return int(bit_number, 2)