class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # zip() : 여러개의 순회 가능한 객체를 인자로 받고 각 객체가 담고있는 원소를 
        # 튜플 형태로 차례로 접근할 수 있는 반복자 반환
        for i, letter_group in enumerate(zip(*strs)):
          # *변수: 해당 매개변수를 가변적인 갯수를 가진 위치 인수로 정의하겠다는 것
          참고: https://hcnoh.github.io/2019-01-27-python-arguments-asterisk
            if len(set(letter_group)) >1:
                return strs[0][:1]
            else:
                return min(strs)
        