class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        strList = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                strList.append("FizzBuzz")
            elif i % 5 == 0:
                strList.append("Buzz")
            elif i % 3 == 0:
                strList.append("Fizz")
            else:
                strList.append(str(i))
        return strList
