/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function mergeTrees(root1: TreeNode | null, root2: TreeNode | null): TreeNode | null {
  const merge = (n1, n2): TreeNode | null => {
    if (!n1) return n2;
    if (!n2) return n1;
    n1.val += n2.val;
    n1.left = merge(n1.left, n2.left);
    n1.right = merge(n1.right, n2.right);
    return n1;

  }
  return merge(root1, root2);

};