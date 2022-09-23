# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math

class Solution:
    def firstBadVersion(self, n: int) -> int:
      left = 0
      right = n

      while left < right :
        middle = left + math.floor((right - left) / 2)
        
        if isBadVersion(middle):
          right = middle
        else:
          left = middle + 1
      return left