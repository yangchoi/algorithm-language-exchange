class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ''.join(filter(str.isalnum, s)).lower() # isalunum: 문자열이 문자면 true return, 아니면 false return
        str2 = ''.join(filter(str.isalnum, s)).lower()[::-1] # [::-1] : 역순으로 처음부터 끝까지 (-1칸)
        return str1 == str2