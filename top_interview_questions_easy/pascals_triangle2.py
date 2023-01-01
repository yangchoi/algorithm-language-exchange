class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        if numRows == 1:
            return answer
        else:
            for i in range(2, numRows+1):
                row_prev = answer[i-2]
                row_curr = [1]
                for n in range(len(row_prev) - 1):
                    row_curr.append(row_prev[n] + row_prev[n+1])
                row_curr.append(1)
                answer.append(row_curr)
            return answer



