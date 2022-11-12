class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
          
        while n != 0:
            n /= 3
            if n == 1:
                return True
        return False