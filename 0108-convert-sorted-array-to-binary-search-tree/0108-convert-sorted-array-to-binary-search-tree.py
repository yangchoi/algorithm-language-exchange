# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def sortToBinarySearch(nums):
            if len(nums) == 0:
                return None
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            root.left = sortToBinarySearch(nums[:middle])
            root.right = sortToBinarySearch(nums[middle + 1 :])
            return root

        return sortToBinarySearch(nums)
