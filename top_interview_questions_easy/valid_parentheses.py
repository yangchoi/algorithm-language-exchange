class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dict = {")": "(",
                "}": "{",
                "]": "["}
        stack = []
        for n in s:
            if n not in dict:
                # 열린 괄호인 경우 stack에 넣음
                stack.append(n)
            # 닫힌 괄호인 경우 가장 최근 아이템과 비교해 같지 않을 경우 거짓
            elif (not stack) or (dict[n] != stack.pop()):
                return False
        return len(stack) == 0





