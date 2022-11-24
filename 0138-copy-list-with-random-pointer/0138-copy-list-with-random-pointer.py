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
        memo = {}
        def deepcopy(n):
            # Trivial returns
            if not n:
                return
            if n in memo:
                return memo[n]

            # 노드 생성 및 임시 저장(순환을 깨기 위함)
            memo[n] = new = Node(n.val)
            # fix node properties
            new.next = deepcopy((n.next))
            new.random = deepcopy(n.random)
            return new
        return deepcopy(head)
