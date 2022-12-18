"""
왼쪽과 오른쪽 각각 depth를 따로 구한다.
왼쪽 값이 있으면 재귀로 maxDepth를 구한다.
left 값을 주고 마지막 return 에서 1 을 더해서 return 해준다.
right 값도 마찬가지.

최종적으로 둘 다 계산이 끝난 경우 둘 중 가장 큰 값(max)을 반환한다.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = 0
        right_depth = 0

        if root.left is not None:
            left_depth = self.maxDepth(root.left)
        if root.right is not None:
            right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

