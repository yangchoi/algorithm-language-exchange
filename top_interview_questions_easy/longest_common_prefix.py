class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        # zip() 여러개 순회 가능한 객체를 인자로 받고 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반복자 반환
        # 튜플을 넘기고 싶은 경우엔 *, 딕셔너리를 넘기고 싶은 경우엔 **
        for n in zip(*strs):
            if(len(set(n))) == 1:
                result += n[0]
            else:
                return result
        return result