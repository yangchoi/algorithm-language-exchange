from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        result = [[1]]

        for i in range(1, numRows):
            row = []
            row.append(1)

            if i > 1:
                for j in range(1, i):
                    row.append(lastRow[j] + lastRow[j - 1])
            row.append(1)

            lastRow = row
            result.append(list(row))
        return result
