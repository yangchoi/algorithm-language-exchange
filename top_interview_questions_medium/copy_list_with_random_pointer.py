"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# input으로 주어지는 linked list 와 같은 linked list 만들기

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashT = dict()
        def DFS(head: 'Node'):
            if head is None:
                return
            if head not in hashT:
                hashT[head] = Node(head.val)
                hashT[head].next = DFS(head.next)
                hashT[head].random = DFS(head.random)
            return hashT[head]
        return DFS{head}
