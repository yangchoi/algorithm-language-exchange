# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        revert = None
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            revert, revert.next, slow = slow, revert, slow.next
            # revert 에 현재 slow
            # revert.next에는 이전 revert 넣어 역순으로 만듦
            # slow에는 정방향으로 진행

        if fast:
            slow = slow.next

        while revert and revert.val == slow.val:
            slow, revert = slow.next, revert.next
        return not revert
