class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        length = 32 - len(s)
        
        for i in range(length):
            s = "0" + s
        return int(s[::-1], 2)