# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        node = ListNode()
        dp = []
        result = []

        while head:
            dp.append(head.val)
            head = head.next
        index = 0
        while index + k <= len(dp):
            temp = dp[index:index+k]
            temp.reverse()
            result += temp
            index = index +k
        result += dp[index:]
        temp = node

        for i in range(len(result)):
            temp.next = ListNode(result[i])
            temp = temp.next
        return node.next

