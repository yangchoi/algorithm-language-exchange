/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
      // null pointer literal
      // ** null은 값이기 때문에 NULL 보다는 nullptr을 사용하는게 더 정확하기 때문에 권장 
      if(list1 == nullptr) return list2;
      if(list2 == nullptr) return list1;

      // 재귀를 통한 구현
      if(list1->val <= list2->val) {
        // 더 큰 값을 다음 Node로 넘긴다.
        ListNode* nextNode = mergeTwoLists(list1->next, list2);
        list1->next = nextNode;
        return list1;
      }else {
        ListNode* nextNode = mergeTwoLists(list1, list2->next);
        list2->next = nextNode;
        return list2;
      }
    }
};