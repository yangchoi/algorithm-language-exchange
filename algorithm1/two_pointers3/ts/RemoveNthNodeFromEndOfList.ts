/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  const dummyHead = new ListNode(0, head);
  let slow = dummyHead;
  let fast = dummyHead;

  // Move fast n nodes ahead of slow
  for (let i = 0; i < n; i++) {
    fast = fast.next;
  }

  // when fast reaches 1st node from the end, slow will be n _ 1th node from the end
  while (fast.next) {
    fast = fast.next;
    slow = slow.next;
  }

  // skip over the noth node form the end
  slow.next = slow.next.next;

  return dummyHead.next;
};
// nth 노드를 제거하는 방법은 없나?