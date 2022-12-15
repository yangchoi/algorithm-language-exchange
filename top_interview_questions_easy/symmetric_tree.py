"""
 root를 확인하고 왼쪽 서브트리와 오른쪽 서브트리를 확인한다.
 대칭인 점을 확인하려면 왼쪽 서브트리와 오른쪽 서브트리를 서로 반대로 비교해야한다.
 두 서브트리의 root를 확인한 후 왼쪽 서브트리의 left가 오른쪽 서브트리의 right와 같은지.
 왼쪽 서브트리의 right가 오른쪽 서브트리의 left와 같은지 비교한다.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSubTreeSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and isSubTreeSymmetric(left.left, right.right) and isSubTreeSymmetric(left.right, right.left)
        return isSubTreeSymmetric(root, root)