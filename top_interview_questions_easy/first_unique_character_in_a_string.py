class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = -1
        s = list(s)
        count = Counter(s)
        i = 0
        
        for chr in s:
            if count[chr] == 1:
                result = i
                break
            i = i + 1
        return result
        