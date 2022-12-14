"""
inorder traversal (정위 순회)
왼쪽 서브트리 > 뿌리노드 > 오른쪽 서브트리
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if node is None:
                pass
            else:
                dfs(node.left)
                result.append(node.val)
                dfs(node.right)

        dfs(root)
        return result