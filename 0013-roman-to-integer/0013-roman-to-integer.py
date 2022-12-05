class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
                      'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000
                  }
        answer = 0
        for i in range(len(s)-1):
            # 앞보다 뒤에 더 큰 값이 나오면 뒤 - 앞의 값을 구한다. 
            if roman[s[i]] < roman[s[i+1]]:
                answer -= roman[s[i]]
            # 그렇지 않은 경우엔 그냥 roman에서 값을 찾아 쓴다. 
            else:
                answer += roman[s[i]]
        # 최종적으로 모든 값을 더한 값이 답이 된다. 
        return answer + roman[s[-1]]