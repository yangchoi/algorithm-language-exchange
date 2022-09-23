import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pivot = 0
        left = 0
        right = len(nums) -1
        
        while(left <= right):
          pivot = math.floor((left + right) / 2)
          
          if nums[pivot] == target:
            return pivot
          elif nums[pivot] > target:
            right = pivot - 1
          else:
            left = pivot + 1
          
        return left
            