class Solution:
    def isPalindrome(self, s: str) -> bool:
        original_s = re.sub('[^0-9a-zA-Zㄱ-힗]', '', s)
        original_s = ''.join(original_s.lower())

        reversed_s = ''.join(reversed(original_s))

        if original_s == reversed_s:
            return True
        else:
            return False