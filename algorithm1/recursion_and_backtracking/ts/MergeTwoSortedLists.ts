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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const head: ListNode = new ListNode();
  let current: ListNode = head;

  while (list1 && list2) {
    // list1 과 list2가 있는 동안
    if (list1.val < list2.val) {
      // list2의 val이 더 크면 
      current.next = list1;
      // 다음 head는 list1이 된다. (그 다음이 list2가 될 것이기 때문)
      list1 = list1.next;
      // list1은 list1.next가 된다.
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }
  current.next = list1 || list2;
  return head.next;
};