class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    # push_back
    def push_back(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    # # push_front(x)
    def push_front(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head  #  4 -> 1(head) -> 2 -> 3 -> None
            self.head = node  # 4(head) -> 1 -> 2 -> 3 -> None

    # Node(1) -> Node(2) -> Node(3) -> None
    # del Node(2).next
    # Node(1) -> Node(2) -> null 0x1298390 <-- Node obj

    # 1 -> 2 -> 3
    # push_front(4)
    # 1(head) -> 2 -> 3
    # 현재: 1 -> 2 -> 3 -> null
    # 목표: 4 -> 1 -> 2 -> 3 -> null
    # head = 1    (head.next == 2)
    # node(4)   {val: 4, next: head}
    # head = 4 -> 1(head) -> 2 -> 3 -> None
    # head = 4(head) -> 1 -> 2 -> 3 -> None

    # 마지막 노드 삭제(x)
    def pop_back(self):
        current = self.head
        while current.next != None:
            if current.next.next == None:
                current.next = None
                return
            current = current.next

    # Current: 1 -> 2 -> None -> None
    # Goal   : 1 -> 2 -> None

    # Current: 1 -> 2 -> None
    # Goal   : 1 -> None

    # step 1. 2까지 이동 하기 (지우려는 노드 바로 직전) -> current
    # step 2. current.next (node3) = None

    # 첫 노드 삭제
    def pop_front(self):
        front = self.head
        self.head = self.head.next
        del front

    def reverseIterative(self):
        # todo

    def reverseRecursive(self):
        #todo (optional)

    def print(self):
        current = self.head
        string = ""
        while current:
            string += str(current.data)
            if current.next:
                string += "->"
            current = current.next
        print(string)


if __name__ == "__main__":
    singlyList = LinkedList()
    singlyList.push_back(Node(1))
    singlyList.push_back(Node(2))
    singlyList.push_back(Node(3))
    singlyList.push_back(Node(4))

    # print(None.next)
    # singlyList.push_front(Node(-1))
    # singlyList.push_back(Node(5))
    # singlyList.print()

    singlyList.pop_back()
    # singlyList.pop_front()

    singlyList.print()
