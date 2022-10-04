function reverseList(head: ListNode | null): ListNode | null {
  // head: 시작 노드 
  // prev: 이전노드(초기값, 맨 처음 시작 노드인 1의 이전 값은 null)
  // nextNode: 다음 노드(while 문에서 초기값을 head.next로 할당)

  let prev = null;

  while (head !== null) {
    let next = head.next;
    head.next = prev;
    prev = head;
    head = next;
  }
  return prev;
}