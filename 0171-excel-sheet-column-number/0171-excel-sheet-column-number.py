class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        nums = 0
        for column in columnTitle:
                nums = nums * 26 + (ord(column) - ord('A') + 1) 
        return nums