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
    int maxDepth(TreeNode* root) {
      if(root == nullptr) return 0;

      if(root -> left == nullptr && root -> right == nullptr) {
        return 1;
      }else {
        int nextLevel = 2;
        return max(dfs(root -> left, nextLevel), dfs(root -> right, nextLevel));
      }
    }

    int dfs(TreeNode* root, int level) {
      if(root == nullptr) {
        return level -1;
      }

      if(root -> left == nullptr && root -> right == nullptr) {
        return level;
      }else {
        int nextLevel = level + 1;
        return max(dfs(root -> left, nextLevel), dfs(root -> right, nextLevel));
      }
    }
};