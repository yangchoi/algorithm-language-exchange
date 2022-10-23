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
    bool isSymmetric(TreeNode* root) {
      if(root == nullptr) return true;

      if(root -> left == nullptr && root -> right == nullptr) return true;
      if(root -> left == nullptr || root -> right == nullptr) return false;

      stack<TreeNode*> dfs;
      dfs.push(root);
      dfs.push(root);
      while(dfs.empty() == false) {
        TreeNode* t1 = dfs.top();
        dfs.pop();
        TreeNode* t2 = dfs.top();
        dfs.pop();

        if(t1 -> val != t2 -> val) {
          return false;
        }
        if(t1 -> left != nullptr && t2 -> right != nullptr) {
          dfs.push(t1 -> left);
          dfs.push(t2 -> right);
        }else if(t1 -> left != nullptr || t2 -> right != nullptr) {
          return false;
        }

        if(t1 -> right != nullptr && t2 -> left != nullptr) {
          dfs.push(t1 -> right);
          dfs.push(t2 -> left);
        }else if(t1 -> right != nullptr || t2 -> left != nullptr) {
          return false;
        }
      }
      return true;
    }
};