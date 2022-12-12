"""
Binary Search를 이용한 문제
left, right 를 두고 left가 right를 초월할 때까지 while loop를 돌린다.
중간값 mid를 정한 다음 mid * mid 값이 x가 될 때까지 left와 right를 조정한다.

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            calc = mid * mid
            if calc == x:
                return mid
            elif calc < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
