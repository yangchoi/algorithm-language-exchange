"""
Recursive 한 방법으로 생각
n번째 계단에 오를 수 있는 방법은 n-1 번째 계단에서 오르는 방법과
n-2 번째 계단에서 오르는 방법 총 두가지. (한번에 계단을 1칸, 혹은 2칸씩 오를 수 있음)
따라서 n번째 계단에 오를 수 있는 경우의 수는 n-1번째 계단에 오를 수 있는 경우의 수에
n-2번째 계단에 오를 수 있는 경우의 수를 더한 값
이는 점화식으로는 F(n) = F(n-1) + F(n-2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array = [0, 1, 2]
        if n < len(dp_array):
            return dp_array[n]

        for i in range(3, n + 1):
            ith_way = dp_array[i-1] + dp_array[i-2]
            dp_array.append(ith_way)
        return dp_array[n]