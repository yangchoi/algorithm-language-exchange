class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while True:
            result = 0
            for x in str(n):
                visited.add(int(x))
                result += intA(x) * int(x)
            
            if result == 1:
                return True
            if result in visited:
                return False
            n = result