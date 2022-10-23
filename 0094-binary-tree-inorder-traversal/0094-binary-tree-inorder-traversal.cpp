/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
      if(root == nullptr) return {};
      
      vector<int> resultList;
      stack<TreeNode*> stack;
      TreeNode* pointer = root;

      while(pointer || !stack.empty()) {
        while(pointer) {
          stack.push(pointer);
          pointer = pointer -> left;
        }

        pointer = stack.top();
        stack.pop();

        resultList.push_back(pointer->val);
        pointer = pointer->right;
      }
      return resultList;
    }
};